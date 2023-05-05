import pygame.font


class Scoreboard:
    def __init__(self, my_game):
        self.screen = my_game.screen
        self.screen_rect = self.screen.get_rect()
        self.stats = my_game.stats
        self.settings = my_game.settings

        # Scoreboard look
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.score_rect = None
        self.score_image = None

        self.manage_score()

    def manage_score(self):
        """Make a rendered image out of score"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
