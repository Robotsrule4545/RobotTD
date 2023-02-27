#!/usr/bin/env python
import pygame
from pygame.locals import *
import os
import sys
import random

screen_height = 400
screen_width = 320
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


class Blaster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=(screen_height / 2, screen_width / 2))
        self.rect = self.image.get_rect(center=(random.randint(0, screen_height), random.randint(0, screen_width)))

    def update(self):
        # placeholder
        pos = pygame.mouse.get_pos()
        if abs(pos[0] - self.rect.x) < 20 and abs(pos[1] - self.rect.y) < 20 and pygame.mouse.get_pressed()[0]:
            self.kill()


def main():
    # Init
    pygame.init()
    last_click = 0
    # Divisible by 80, 10x8 grid of 16x16 squares.
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption('Robot\'s Tower Defense')
    icon = pygame.transform.scale(load_image("icon.png"), (128, 128))
    pygame.display.set_icon(icon)

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    blaster_group = pygame.sprite.Group()

    # Update loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(True)
            if event.type == pygame.MOUSEBUTTONDOWN:
                blaster = Blaster()
                blaster_group.add(blaster)
                last_click = pygame.time.get_ticks()
        if pygame.time.get_ticks() > 10000 + last_click:
            exit(True)

        # Add update code here.

        screen.blit(background, (0, 0))

        blaster_group.draw(screen)
        blaster_group.update()
        # Might be a problem when the background gets pasted over sprites
        pygame.display.flip()


if __name__ == '__main__':
    main()
