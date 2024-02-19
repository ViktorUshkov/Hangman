import sys
import pygame
from settings import Settings

class Hangman:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Hangman')

        self.background = pygame.image.load('assets/background.jpg')
        self.background = pygame.transform.scale(self.background,
                                                 (self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        while True:
            self._check_events()
            self._update_window()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button_click(mouse_position)

    def _check_play_button_click(self, mouse_position):
        pass

    def _update_window(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()