import sys
import pygame
import random

from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import upgrade_items


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        pygame.display.set_icon(self.settings.icon_image)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.upgrades = pygame.sprite.Group()

        self._create_army()

        # Create Play button
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """All the processes run here"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.move_update()
                self._update_bullets()
                self._update_aliens()
                self._update_upgrades()
            self._update_screen()
            # Limit the max fps
            self.clock.tick(self.settings.max_fps)

    def _check_events(self):
        """Respond to the pushed keys and other events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif not self.stats.game_active and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start new game if play button pushed"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Hide mouse cursor
            pygame.mouse.set_visible(False)
            # Reset statistics
            self.stats.stats_reset()
            self.stats.game_active = True
            # Reset speed of the game
            self.settings.init_dynamic_settings()
            # Player can start game again after losing,
            # so we need to get rid of aliens and bullets from previous game
            self.aliens.empty()
            self.bullets.empty()
            # Set everything for new game
            self._create_army()
            self.scoreboard.manage_score()
            self.scoreboard.manage_lives()

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

    def _check_alien_bullet_collision(self):
        """Function delete colliding bullets, and create new army if all aliens are dead,
        also with a certain probability create upgrades"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Add points for eliminated aliens
        if collisions:
            for dead_aliens in collisions.values():
                # By a certain chance create upgrade
                if random.randint(1, 20) == 7:
                    self._create_upgrade(dead_aliens)

                # Add points for dead aliens
                self.stats.score += self.settings.alien_points * len(dead_aliens)
            self.scoreboard.manage_score()

        # When all aliens are dead, new wave appears
        if not self.aliens:
            self.bullets.empty()
            self._create_army()
            # Increase difficulty after destroying whole army
            self.settings.increase_difficulty()

    def _check_upgrade_ship_collision(self):
        """Check if ship touch the upgrade, activate upgrade if so"""
        for upgrade in self.upgrades.sprites():
            if self.ship.rect.colliderect(upgrade.rect):
                upgrade.activate_upgrade()
                upgrade.kill()

    def _check_aliens_reach_bottom(self):
        """Check if aliens reach the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_destroy()
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

    def _create_upgrade(self, alien):
        """Create random upgrade and place it where alien died"""
        upgrades = [upgrade_items.BulletSpeedUpgrade(self, alien[0]),
                    upgrade_items.ShipSpeedUpgrade(self, alien[0])]
        new_upgrade = random.choice(upgrades)
        self.upgrades.add(new_upgrade)

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

    def _update_aliens(self):
        """Update aliens position"""
        self._check_army_edge()
        self.aliens.update()

        # Find the aliens that touch the ship, start game with new live if so
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_destroy()

        # Look for the aliens that touches the bottom
        self._check_aliens_reach_bottom()

    def _update_bullets(self):
        """Update the position of bullets, remove extra bullets when they
        go out of the screen, check collision between bullets and aliens"""
        self.bullets.update()
        self._remove_extra_bullets()
        self._check_alien_bullet_collision()

    def _update_upgrades(self):
        """Update the position of upgrades, remove extra upgrades when they
         go out of the screen, check collisions between upgrades and ship"""
        self.upgrades.update()
        self._remove_extra_upgrades()
        self._check_upgrade_ship_collision()

    def _update_screen(self):
        """Update the images on screen and flips to the next screen"""
        self.screen.fill(self.settings.bg_color)

        # Draw the 'Play' button if game is not active
        if self.stats.game_active:
            self.scoreboard.display_score()
            self.ship.blit_me()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            for upgrade in self.upgrades.sprites():
                upgrade.draw_upgrade()
            self.aliens.draw(self.screen)
        else:
            self.play_button.draw_button()

        pygame.display.update()

    def _remove_extra_bullets(self):
        """Remove bullets that are behind the screen"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _remove_extra_upgrades(self):
        """Remove upgrades that are behind the screen"""
        for upgrade in self.upgrades:
            if upgrade.rect.top == self.screen.get_rect().bottom:
                self.upgrades.remove(upgrade)

    def _ship_destroy(self):
        """Respond when ship is destroyed"""
        self.stats.ship_live_count -= 1

        # Change number of lives on scoreboard
        self.scoreboard.manage_lives()

        # Deactivate game if we don't have lives
        if self.stats.ship_live_count == 0:
            self.stats.game_active = False
            # Make cursor visible again
            pygame.mouse.set_visible(True)
            return

        # Remove bullets and aliens
        self.aliens.empty()
        self.bullets.empty()

        # Set everything for the new start
        self._create_army()
        self.ship.center_ship()

        # Add a little delay
        sleep(0.5)


if __name__ == '__main__':
    aliens = AlienInvasion()
    aliens.run_game()
