"""
This is a basic class to be used for making a game app.

All different game modules should inherit from this.
"""

import os
import glob
import sys

import pygame
from pygame.locals import *

from Pygame.Example.project_settings import *


class App(object):

    def __init__(self):
        self.game_loop = True

    def update(self):
        pass

    def draw(self):
        pass

    def loop(self):
        while self.game_loop:
            self.event()

            self.update()

            self.draw()

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# RESOURCE LEVEL
def load_resources():
    """Will properly load .png and .ogg files
    producing a 'filename':pygameobject dictionary
    """
    workingDirectory = os.path.split(__file__)[0] + "/"

    images = []
    sounds = []

    subDirsToExplore = 3
    actualDir = ""
    for i in range(subDirsToExplore):
        actualDir = actualDir + "*/"

        for image in glob.glob(workingDirectory + actualDir + '*.png'):
            images.append(image)
        for sound in glob.glob(workingDirectory + actualDir + '*.ogg'):
            sounds.append(sound)

    resources = {}

    for image in images:
        imageName = os.path.split(image)[1]
        resources[imageName] = load_image(image)
    for sound in sounds:
        soundName = os.path.split(sound)[1]
        resources[soundName] = load_sound(sound)

    return resources


def load_image(path):
    """Return surface from full image path
    """
    try:
        image = pygame.image.load(path)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', path)
        raise SystemExit(message)
    return image, image.get_rect()


def load_sound(path):
    return None


def main():
    game = App()
    game.loop()


if __name__ == "__main__":
    main()