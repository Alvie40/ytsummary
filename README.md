# ytsummary

ytsummary is a Python-based tool designed to download and summarize subtitles from YouTube videos. This tool leverages `yt-dlp` for downloading subtitles and `Cython` for optimizing performance.

## Features

- Download subtitles from YouTube videos
- Clean and summarize subtitles by removing timestamps and HTML tags
- Optimized for performance using Cython

## Requirements

- Python 3.12 or higher
- `yt-dlp`
- `Cython`
- `setuptools` and `wheel` for building

## Installation

1. **Install Python and dependencies:**

    ```sh
    pyenv install 3.12.4
    pyenv global 3.12.4
    ```

2. **Install Poetry:**

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

3. **Clone the repository:**

    ```sh
    git clone https://github.com/alvie40/ytsummary.git
    cd ytsummary
    ```

4. **Install project dependencies:**

    ```sh
    poetry install
    ```

5. **Build the project:**

    ```sh
    poetry run python setup.py build_ext --inplace
    ```

## Usage

Run the tool with the following command:

```sh
poetry run python -m ytsummary "https://www.youtube.com/watch?v=VIDEO_ID"
