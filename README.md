# YouTube Downloader
Simple Python Tool to download videos and audios from YouTube.

## Install
First make sure you have `ffmpeg` installed on your computer. FFMpeg is used to transform our video into a audio file.

### Virtual Environment
To install on a virtual environment:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Globally
To install requirements globally:
```
$ pip3 install -r requirements.txt
```

## Running

### Download Video
```bash
$ python download.py --link YOUTUBE_LINK
```

### Download Audio
```bash
$ python download.py --link YOUTUBE_LINK --type 1
```

### Extra Flags
- *Output* - Default is set to `download.py` directory.
- *Filename* - Deafault is set to `output`.
