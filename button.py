from typing import Tuple

import pygame

class Button:
    """
    Класс, описывающий одну кнопку
    """
    BUTTON_WIDTH = 20
    BUTTON_HEIGHT = 20

    LIGHT_SKY_BLUE = (135, 206, 250)
    BLACK = (0, 0, 0)

    START_CHAR = ord('a')

    START_CENTER_X = 0.0
    START_CENTER_Y = 0.0

    def __init__(self, hangman):
        """
        Инициализация класса кнопки
        :param hangman: экземпляр основного класса игры
        """
        # настройки экрана
        self.screen = hangman.screen
        self.screen_rect = hangman.screen.get_rect()

        # настройки кнопки
        self.width = self.BUTTON_WIDTH
        self.height = self.BUTTON_HEIGHT
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = None
        self.color = self.LIGHT_SKY_BLUE
        self.textcolor = self.BLACK
        self.font = pygame.font.Font(None, 48)

        # статус кнопки: в случае True отрисовываем кнопку, после нажатия меняем на False и не отрисовываем
        self.active = True

        # буква на кнопке
        self.char = None
        self.char_img = None
        self.char_img_rect = None

    def assign_center(self, offset_x: float, offset_y: float) -> tuple[float, float]:
        """
        Возвращает координаты центра кнопки
        :param offset_x: отступ от первой кнопки (с буквой А) по оси Х
        :param offset_y: отступ от первого ряда кнопок (по оси Y)
        :return: координаты центра для кнопки
        """
        return self.START_CENTER_X + offset_x, self.START_CENTER_Y + offset_y

    def assign_char(self, offset: int) -> str:
        """
        Возвращает букву для кнопки
        :param offset: отступ от буквы 'A' в алфавите
        :return: буква на кнопке
        """
        return chr(self.START_CHAR + offset)

    def display_char(self) -> None:
        """
        Задает Rect подписи кнопки (буквы) для последующей отрисовки
        """
        self.char_img = self.font.render(self.char, True, self.textcolor, self.color)
        self.char_img_rect = self.char_img.get_rect()
        self.char_img_rect.center = self.rect.center

class ButtonsSet:
    """
    Класс для работы с множеством кнопок
    """
    ALPHABET_SIZE = 26

    def __init__(self, hangman):
        """
        Инициализация класса множества кнопок
        :param hangman: экземпляр основного класса игры
        """
        self.buttons = self._load_buttons(hangman)

    def _load_buttons(self, hangman) -> list[Button]:
        """
        Инициализирует список игровых кнопок
        :param hangman: экземпляр основного класса игры
        :return: список кнопок
        """
        buttons = []
        for i in range(self.ALPHABET_SIZE):
            new_button = Button(hangman)
            # new_button.assign_center()
            # new_button.assign_char()
            # new_button.display_char()
            buttons.append(new_button)
        return buttons

    def blit_buttons(self) -> None:
        """
        Отрисовка кнопок
        """
        ...