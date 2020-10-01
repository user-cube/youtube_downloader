from pytube import YouTube
import argparse
import coloredlogs
import logging
import subprocess

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


def download_video(yt):
    ys = yt.streams.get_highest_resolution()

    logger.info("....:: Downloading ::....")

    ys.download(output_path=OUTPUT, filename=FILENAME.replace(" ", "_"))

    logger.info("....:: Download Completed ::....")

def download_audio(yt):
    ys = yt.streams.get_audio_only()
    logger.info("....:: Downloading ::....")

    outfile = ys.download(output_path=OUTPUT, filename=FILENAME.replace(" ", "_"))
    mp4 = outfile
    mp3 = outfile.replace(".mp4", ".mp3").split("/")[-1]
    ffmpeg = ('ffmpeg -i %s ' % mp4 +  OUTPUT + mp3)
    subprocess.call(ffmpeg, shell=True)
    subprocess.call("rm " + outfile, shell=True)

    logger.info("....:: Download Completed ::....")

def print_info(yt):
    logger.info("....:: Youtube Video Info ::....")
    logger.info("Title => " + yt.title)
    logger.info("Number of views => " + str(yt.views))
    logger.info("Length of video => " + str(yt.length))
    logger.info("Rating of video => " + str(yt.rating))

def define_properties():
    if LINK is not None:
        yt = YouTube(LINK)
        print_info(yt)
        if DOWNLOAD_TYPE == 0:
            download_video(yt)
        else:
            download_audio(yt)
    else:
        logger.error("No Link")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--link", help="Youtube Link", default=None)
    parser.add_argument("--type", help="0 - Video; 1 - Audio", default=0, type=int)
    parser.add_argument("--output", help="Output directory", default="")
    parser.add_argument("--filename", help="Output file", default="output")
    args = parser.parse_args()
    LINK = args.link
    DOWNLOAD_TYPE = args.type
    OUTPUT = args.output
    FILENAME = args.filename
    define_properties()
