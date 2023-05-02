import pygame


class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.max_fps = 120

        # Icon settings
        self.icon_image = pygame.image.load('images/mokash_icon.png')

        # Ship settings
        self.ship_speed = 3
        self.ship_limit = 1

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3

        # Alien settings
        self.aliens_speed = 2.5
        self.aliens_down_speed = 50
        self.aliens_direction = 1
