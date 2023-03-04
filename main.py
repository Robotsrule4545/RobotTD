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
    return surface.convert_alpha()


def get_angle(y2, y1, x2, x1):
    adjacent = int(y2) - int(y1)
    opposite = int(x2) - int(x1)
    angle = int(opposite / adjacent)
    return angle


def get_out_of_range(y2, y1, x2, x1, t_range):
    in_range = True
    a = int(y2) - int(y1)
    o = int(x2) - int(x1)
    if a > t_range or o > t_range:
        in_range = False
    else:
        in_range = True
    return in_range


def exit(e):
    if e:
        pygame.quit()
        print("Quitting")
        sys.exit()


class Blaster(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images = []
        self.images.append(pygame.transform.scale(load_image("blaster.png"), (80,80)))
        self.images.append(load_image("blaster1.png"))
        self.image_num = 0
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

    def update(self):
        print("updated")
        # placeholder[0]


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((18,8))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(0, 0))

    def update(self):
        self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        ex = "placeholder"
        ey = "placeholder"


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
    background.fill((178, 246, 247))

    blaster_group = pygame.sprite.Group()

    # Update loop
    while True:
        current_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(True)
                print("quitting!")
            if event.type == pygame.MOUSEBUTTONDOWN:  # and placing_ready == True:
                blaster = Blaster(current_mouse_pos)
                blaster_group.add(blaster)

        # update stuff
        blaster_group.update()

        # drawing
        screen.blit(background, (0, 0))
        blaster_group.draw(screen)
        # blaster_group.update(current_mouse_pos)
        # Might be a problem when the background gets pasted over sprites
        pygame.display.flip()


if __name__ == '__main__':
    main()
    print("starting!")
