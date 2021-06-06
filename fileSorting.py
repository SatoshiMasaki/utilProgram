from glob import glob
import os
import shutil
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4

MP3_FILE = "*.mp3"
MP4_FILE = "*.mp4"
ASMR_FILE = "*ASMR*"
MAIN_DIR = r"C:\Users\umbre\download_video"


def getMP3Length(path):
    try:
        audio = MP3(path)
        length = audio.info.length
        return length
    except:
        return None


def getMP4Length(path):
    try:
        audio = MP4(path)
        length = audio.info.length
        return length
    except:
        return None


def main():
    os.chdir(MAIN_DIR)
    asmr_files = glob(ASMR_FILE)


if __name__ == '__main__':
    main()
