import subprocess
import sys


def download_video(video_url):
    try:
        subprocess.run(
            [
                'yt-dlp',
                '-f',
                'bestvideo+bestaudio',
                '-o',
                '%(title)s.%(ext)s',
                video_url,
            ],
            check=True,
        )
        print('Video downloaded successfully.')
    except subprocess.CalledProcessError as e:
        print(f'An error occurred: {e}')


def main():
    EXPECTED_ARG_COUNT = 2
    if len(sys.argv) != EXPECTED_ARG_COUNT:
        print('Usage: ytvideo <YouTube video URL>')
        sys.exit(1)

    video_url = sys.argv[1]
    download_video(video_url)
