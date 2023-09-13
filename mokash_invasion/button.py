import pygame.font


class Button:
    def __init__(self, my_game, message):
        """Button initialization"""
        self.screen = my_game.screen
        self.screen_rect = my_game.screen.get_rect()
        self.settings = my_game.settings

        # Set the button properties
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = self.settings.custom_font

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._manage_button(message)

    def _manage_button(self, message):
        """Center the text of button"""
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)
