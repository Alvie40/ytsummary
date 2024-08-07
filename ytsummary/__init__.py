import os
import subprocess

def download_subtitles(video_url):
    try:
        video_id = subprocess.check_output(['yt-dlp', '--get-id', video_url], text=True).strip()
        subtitle_file = f"{video_id}.en.vtt"
        output_file = f"{video_id}_summary.txt"

        subprocess.run(['yt-dlp', '--write-auto-sub', '--sub-lang', 'en', '--sub-format', 'vtt', '-o', f"{video_id}.%(ext)s", video_url], check=True)

        if os.path.isfile(subtitle_file):
            with open(subtitle_file, 'r') as f:
                lines = f.readlines()

            with open(output_file, 'w') as f:
                prev_line = ""
                for line in lines:
                    if not line.startswith(('0', '\n')) and line != prev_line:
                        clean_line = ''.join(c for c in line if c not in '<>')  # Removing simple HTML tags
                        f.write(clean_line)
                        prev_line = line

            os.remove(subtitle_file)
            print(f"Subtitles saved in {output_file}")
        else:
            print("Failed to download subtitles.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python -m ytsummary <YouTube video URL>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_subtitles(video_url)
