import pygame


class Ship:
    def __init__(self, my_game):
        """Initializing the ship and defining the starting position."""
        self.screen = my_game.screen
        self.settings = my_game.settings
        self.screen_rect = my_game.screen.get_rect()

        # Different images for the left and right direction of ship
        self.image_face_left = pygame.image.load('mokash_invasion/images/dababy_mokash_ship_left.png')
        self.image_face_right = pygame.image.load('mokash_invasion/images/dababy_mokash_ship_right.png')
        self.image = self.image_face_left

        self.rect = self.image_face_left.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Storing the initial horizontal position of ship
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def blit_me(self):
        """Draw ship at its current position"""
        self.screen.blit(self.image, self.rect)

    def move_update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            # Change image to right facing picture when moving right
            self.image = self.image_face_right
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # Change image to right facing picture when moving left
            self.image = self.image_face_left

        self.rect.x = self.x

    def center_ship(self):
        """Place ship in the center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
