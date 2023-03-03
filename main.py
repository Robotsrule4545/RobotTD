import pygame
from pygame.locals import *
import os
import sys
import math

screen_height = 400
screen_width = 320
placing_ready = False
pausedGame = False
print("Reading!")

main_dir = os.path.split(os.path.abspath(__file__))[0]

print("Defining functions!")


def load_image(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "assets", file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit(f'Could not load image "{file}" {pygame.get_error()}')
    return surface.convert()


def get_angle(y2, y1, x2, x1):
    adjacent = int(y2) - int(y1)
    opposite = int(x2) - int(x1)
    angle = int(opposite / adjacent)
    return angle


def get_outofrange(y2, y1, x2, x1, range):
    inRange = True
    a = int(y2) - int(y1)
    o = int(x2) - int(x1)
    if a > range or o > range:
        inRange = False
    else:
        inRange = True
    return inRange


def exit(e):
    if e:
        pygame.quit()
        print("Quitting")
        sys.exit()


class Blaster(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

    def update(self):
        # placeholder
        pos = pygame.mouse.get_pos()
        if abs(pos[0] - self.rect.x) < 20 and abs(pos[1] - self.rect.y) < 20 and pygame.mouse.get_pressed()[0]:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    print("placeholder")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(255, 0, 0)
        self.rect = self.image.get_rect()

    def update(self):
        enemyX = "placeholder"
        enemyY = "placeholder"


def main():
    # Init
    pygame.init()
    # Divisible by 80, 10x8 grid of 16x16 squares.
    # pygame.display.set_caption('Robot\'s Tower Defense')
    pygame.display.set_caption("Tower Defense*")
    print("initializing!")
    screen = pygame.display.set_mode((800, 640))
    icon = load_image("icon.png")
    pygame.display.set_icon(icon)

    background = pygame.Surface(screen.get_size())
    background = background.convert()

    blaster_group = pygame.sprite.Group()

    # Update loop
    while True:
        current_mouse_pos = pygame.mouse.get_pos()
        print("updated!")
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(True)
                print("quitting!")
            if event.type == pygame.MOUSEBUTTONDOWN:  # and placing_ready == True:
                blaster = Blaster(current_mouse_pos)
                blaster_group.add(blaster)
        screen.blit(background, (0, 0))

        blaster_group.draw(screen)
        # blaster_group.update(current_mouse_pos)
        # Might be a problem when the background gets pasted over sprites
        pygame.display.flip()


if __name__ == '__main__':
    main()
    print("starting!")
