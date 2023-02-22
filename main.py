#!/usr/bin/env python
import pygame
from pygame.locals import *
import towers.blaster
import os
import sys
# import numpy


main_dir = os.path.split(os.path.abspath(__file__))[0]


def load_image(file):
    file = os.path.join(main_dir, "assets", file)
    surface = pygame.image.load(file)
    return surface.convert()


def exit(bool):
    if bool:
        pygame.quit()
        sys.exit()


def main():
    # Init
    pygame.init()

    # Dividable by 80, 10x8 grid of 16x16 squares.
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption('Robot\'s Tower Defense')
    icon = pygame.transform.scale(load_image("icon.png"), (128, 128))
    pygame.display.set_icon(icon)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Update loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(True)
        # Add update code here.
        screen.blit(background, (0, 0))
        # Might be a problem when the background gets pasted over sprites
        pygame.display.flip()


if __name__ == '__main__':
    main()
