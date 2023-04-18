import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Mokash Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.move_update()
            self._update_screen()


    def _check_events(self):
        """Responds to the pushed keys and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Updates the images on screen and flips to the next screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.update()


if __name__ == '__main__':
    aliens = AlienInvasion()
    aliens.run_game()
