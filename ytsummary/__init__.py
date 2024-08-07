import os
import subprocess
import sys


def clean_line(line):
    """Remove HTML tags and leading/trailing whitespace from a line."""
    return ''.join(c for c in line if c not in '<>').strip()


def download_subtitles(video_url):
    try:
        video_id = subprocess.check_output(
            ['yt-dlp', '--get-id', video_url], text=True
        ).strip()
        subtitle_file = f'{video_id}.en.vtt'
        output_file = f'{video_id}_summary.txt'

        subprocess.run(
            [
                'yt-dlp',
                '--write-auto-sub',
                '--sub-lang',
                'en',
                '--sub-format',
                'vtt',
                '-o',
                f'{video_id}.%(ext)s',
                video_url,
            ],
            check=True,
        )

        if os.path.isfile(subtitle_file):
            with open(subtitle_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            with open(output_file, 'w', encoding='utf-8') as f:
                seen_lines = set()
                for line in lines:
                    clean_line_content = clean_line(line)
                    # Skip empty lines and lines that start with timestamps
                    if not clean_line_content or line.startswith(('0', '\n')):
                        continue
                    if clean_line_content not in seen_lines:
                        f.write(clean_line_content + '\n')
                        seen_lines.add(clean_line_content)

            os.remove(subtitle_file)
            print(f'Subtitles saved in {output_file}')
        else:
            print('Failed to download subtitles.')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')


def main():
    EXPECTED_ARG_COUNT = 2
    if len(sys.argv) != EXPECTED_ARG_COUNT:
        print('Usage: ytsummary <YouTube video URL>')
        sys.exit(1)

    video_url = sys.argv[1]
    download_subtitles(video_url)
