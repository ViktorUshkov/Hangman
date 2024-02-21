import sys
import pygame
import random
from settings import Settings
from hangtheman import HangTheMan
from button import ButtonsSet

class Hangman:
    """
    Основной класс игры
    """
    # файл со словами для игры
    FILE_WITH_WORDS = "words.txt"
    def __init__(self):
        """
        Инициализация класса игры, установка настроек
        """
        pygame.init()
        # настройки приложения
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Hangman')
        self.background = pygame.image.load('assets/background.jpg')
        self.background = pygame.transform.scale(self.background,
                                                 (self.settings.screen_width, self.settings.screen_height))
        # загаданное слово
        self.mystery_word = None
        # строка для отслеживания отгадывания mystery_word
        self.guessing_word = None
        # количество ошибок при угадывании
        self.faults = 0
        self.hangtheman = HangTheMan(self)
        self.buttons = ButtonsSet(self)

    def run_game(self) -> None:
        """
        Функция цикла приложения: приложение работает, пока в методе _check_events не придет событие QUIT
        """
        while True:
            self._check_events()
            self._update_window()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """
        Обработка событий игры, таких как нажатия клавиш, закрытие окна приложения
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button_click(mouse_position)

    def _check_play_button_click(self, mouse_position) -> None:
        """
        Обработка кликов мыши
        :param mouse_position: позиция, в которой произошел клик
        """
        pass

    def _update_window(self) -> None:
        """
        Отрисовка окна приложения
        """
        self.screen.blit(self.background, (0, 0))
        self.hangtheman.blitme(self)
        self.buttons.blit_buttons()
        pygame.display.flip()

    def _get_word(self) -> str:
        """
        Получение нового случайного слова для игры из файла со словами
        :return: слово для игры
        """
        with open(self.FILE_WITH_WORDS, 'r') as file:
            all_words: list[str] = file.readlines()
        return all_words[random.randrange(0, len(all_words) - 1)].rstrip()

    def _is_guess_right(self, letter: str) -> bool:
        """
        Проверяет, есть ли выбранная буква в слове
        :return: True, если буква в слове; False в ином случае
        """
        return letter in self.mystery_word
