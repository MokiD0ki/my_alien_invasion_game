import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, my_game):
        super().__init__()
        self.screen = my_game.screen

        self.image = pygame.image.load('images/mokash_alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
