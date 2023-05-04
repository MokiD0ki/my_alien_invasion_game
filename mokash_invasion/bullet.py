import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, my_game):
        super().__init__()
        self.screen = my_game.screen
        self.settings = my_game.settings
        self.color = my_game.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = my_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Update the position of the bullet"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
