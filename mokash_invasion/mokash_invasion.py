import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        pygame.display.set_icon(self.settings.icon_image)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Mokash Invasion")

        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_army()

    def run_game(self):
        """All the processes tun here"""
        while True:
            self._check_events()
            self.ship.move_update()
            self._update_bullets()
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
        """Checks the keys that was pushed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.   K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """Checks the keys that was released"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_army(self):
        """Creates the army of aliens"""
        alien = Alien(self)
        self.aliens.add(alien)
 
        # Calculating how much aliens we can have on horizontal row
        max_aliens = self._alien_num_calculator(alien)

        for alien_num in range(max_aliens):
            self._create_alien(alien_num)

    def _alien_num_calculator(self, alien):
        """Calculates the number of aliens that can fit on the screen"""
        alien_width = alien.rect.width
        free_space_x = self.settings.screen_width - (2 * alien_width)
        return free_space_x // (alien_width * 2)

    def _create_alien(self, alien_num):
        """Creates an alien considering the resolution of window"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _fire_bullet(self):
        """Creates bullet and adds it in the group of other bullets"""
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _remove_extra_bullets(self):
        """Removes bullets that are behind the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_bullets(self):
        self.bullets.update()
        self._remove_extra_bullets()

    def _update_screen(self):
        """Updates the images on screen and flips to the next screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    aliens = AlienInvasion()
    aliens.run_game()
