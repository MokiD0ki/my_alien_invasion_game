import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, my_game):
        super().__init__()
        self.screen = my_game.screen
        self.settings = my_game.settings
        self.image = pygame.image.load('images/mokash_alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.x < self.settings.screen_width:
            self.x += (self.settings.aliens_speed * self.settings.aliens_direction)
            self.rect.x = self.x

    def edge_touching(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        return True if self.rect.right >= screen_rect.right or self.rect.left <= 0 else False
