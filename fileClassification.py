from glob import glob
import os
import shutil


MP3 = "*.mp3"
MP4 = "*.mp4"


def main():
    dirname = input("ディレクトリのパスを入れてください : ")
    os.chdir(dirname)
    filename = dirname[dirname.rfind("\\") + 1:]

    mp3_files = glob(MP3)
    mp4_files = glob(MP4)
    make_filename_mp3 = filename + "_mp3"
    make_filename_mp4 = filename + "_mp4"

    if not os.path.exists(make_filename_mp3):
        os.mkdir(make_filename_mp3)
    if not os.path.exists(make_filename_mp4):
        os.mkdir(make_filename_mp4)

    for file in mp3_files:
        shutil.move(file, make_filename_mp3)

    for file in mp4_files:
        shutil.move(file, make_filename_mp4)


if __name__ == '__main__':
    main()
