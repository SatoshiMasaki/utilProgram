from mutagen.mp3 import MP3
import pygame
import time

DEFAULT_SOUND = 'soundFile/decision1.mp3'


def sound(filename=DEFAULT_SOUND, playback_time=None):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    if playback_time is None:
        mp3_length = MP3(filename).info.length
    else:
        mp3_length = playback_time

    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()


def alarm(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    mp3_length = MP3(filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()


if __name__ == '__main__':
    sound()

