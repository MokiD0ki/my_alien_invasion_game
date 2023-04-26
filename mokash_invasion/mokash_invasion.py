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
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Respond to the pushed keys and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Check the keys that was pushed"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.   K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """Check the keys that was released"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_army_edge(self):
        """Check if army reached the edges of screen, change direction if it's so"""
        for alien in self.aliens.sprites():
            if alien.edge_touching():
                self._change_army_direction()
                break

    def _change_army_direction(self):
        """Army of aliens go down and then change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.aliens_down_speed
        self.settings.aliens_direction *= -1

    def _alien_num_calculator(self, alien):
        """Calculate the number of aliens that can fit on the screen"""
        alien_width = alien.rect.width
        free_space_x = self.settings.screen_width - (2 * alien_width)
        return free_space_x // (alien_width * 2)

    def _create_army(self):
        """Create 3 rows of aliens"""
        alien = Alien(self)
        self.aliens.add(alien)
 
        # Calculating how much aliens we can have on horizontal row
        max_aliens = self._alien_num_calculator(alien)

        for row_index in range(3):
            for alien_num in range(max_aliens):
                self._create_alien(alien_num, row=row_index)

    def _create_alien(self, alien_num, row):
        """Create an alien considering the resolution of window"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_num
        alien.y += (row * alien.y * 2)

        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _fire_bullet(self):
        """Create bullet and adds it in the group of other bullets"""
        if len(self.bullets) < self.settings.bullet_max:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _remove_extra_bullets(self):
        """Remove bullets that are behind the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        self._check_army_edge()
        self.aliens.update()

    def _update_bullets(self):
        """update the position of bullets, remove extra bullets when
                it collides with aliens or goes out of the screen"""
        self.bullets.update()
        self._remove_extra_bullets()

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_screen(self):
        """Update the images on screen and flips to the next screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    aliens = AlienInvasion()
    aliens.run_game()
