import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Icon settings
        self.icon_image = pygame.image.load('images/mokash_icon.png')

        # Ship settings
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 0.7
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3
