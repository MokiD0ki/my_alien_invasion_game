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

        # Game font
        self.custom_font = pygame.font.Font('fonts/Pixeltype.ttf', 48)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_max = 3

        # Alien settings
        self.aliens_down_speed = 5

        # Game progression
        self.speed_progression = 1.2
        self.score_progression = 1.5

        # Dynamic settings
        self.ship_speed = 0
        self.aliens_speed = 0
        self.bullet_speed = 0
        self.aliens_direction = 0
        self.alien_points = 0

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Initialize settings that change during the game"""
        self.ship_speed = 3
        self.aliens_speed = 2.5
        self.bullet_speed = 3

        # Aliens move right when 1 and left when -1
        self.aliens_direction = 1

        # Scoring
        self.alien_points = 20

    def increase_difficulty(self):
        """Increase difficulty by increasing speed of aliens"""
        self.aliens_speed *= self.speed_progression
        self.ship_speed *= self.speed_progression
        self.bullet_speed *= self.speed_progression
        self.alien_points = int(self.alien_points * self.score_progression)
