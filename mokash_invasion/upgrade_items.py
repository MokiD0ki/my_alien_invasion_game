import pygame
from alien import Alien
from pygame.sprite import Sprite


class UpgradeItem(Sprite):
    def __init__(self, mygame, item_color, size_x, size_y, alien: Alien):
        super().__init__()
        self.settings = mygame.settings
        self.screen = mygame.screen
        self.color = item_color

        self.rect = pygame.Rect(0, 0, size_x, size_y)
        self.rect.center = alien.rect.center

        self.y = float(self.rect.y)

    def update(self):
        """Update the position of upgrade item"""
        self.y += self.settings.item_down_speed
        self.rect.y = self.y

    def draw_upgrade(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class BulletSpeedUpgrade(UpgradeItem):
    def __init__(self, mygame, alien):
        super().__init__(mygame, 'green', 30, 30, alien)

    def activate_upgrade(self):
        self.settings.bullet_speed += 2
