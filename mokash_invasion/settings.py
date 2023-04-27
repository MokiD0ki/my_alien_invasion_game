import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Icon settings
        self.icon_image = pygame.image.load('images/mokash_icon.png')

        # Ship settings
        self.ship_speed = 0.9
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 0.7
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 4

        # Alien settings
        self.aliens_speed = 1.5
        self.aliens_down_speed = 40
        self.aliens_direction = 1
