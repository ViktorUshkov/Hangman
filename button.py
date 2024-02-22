from math import ceil

import pygame
from settings import Settings

class Button:
    """
    Класс, описывающий одну кнопку
    """
    # радиус
    RADIUS = 24
    # расстояние между центрами кнопок по оси X
    DIST_BETWEEN_BUTTONS_X = 2.5 * RADIUS
    # расстояние между центрами кнопок по оси Y
    DIST_BETWEEN_BUTTONS_Y = 2.5 * RADIUS

    # константы для цвета кнопки и текста
    LIGHT_SKY_BLUE = (135, 206, 250)
    BLACK = (0, 0, 0)
    # обводка кнопки
    OUTLINE = 2

    # код буквы на первой кнопке
    START_CHAR = ord('a')

    # координаты центра первой буквы
    START_CENTER_X = 43
    START_CENTER_Y = Settings.SCREEN_HEIGHT * (2 / 3) + 50

    def __init__(self, hangman):
        """
        Инициализация класса кнопки
        :param hangman: экземпляр основного класса игры
        """
        # настройки экрана
        self.screen = hangman.screen
        self.screen_rect = hangman.screen.get_rect()

        # настройки кнопки
        self.radius = self.RADIUS
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.color = self.LIGHT_SKY_BLUE
        self.textcolor = self.BLACK
        self.font = pygame.font.Font(None, 48)

        # статус кнопки: в случае True отрисовываем кнопку, после нажатия меняем на False и не отрисовываем
        self.active = True

        # буква на кнопке
        self.char = None
        self.char_img = None
        self.char_img_rect = None

    def assign_center(self, offset_x: int, offset_y: int) -> tuple[float, float]:
        """
        Возвращает координаты центра кнопки
        :param offset_x: отступ от первой кнопки (с буквой А) по оси Х (в кнопках)
        :param offset_y: отступ от первого ряда кнопок (по оси Y, в кнопках)
        :return: координаты центра для кнопки
        """
        return self.START_CENTER_X + offset_x * self.DIST_BETWEEN_BUTTONS_X, \
            self.START_CENTER_Y + offset_y * self.DIST_BETWEEN_BUTTONS_Y

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
    # количество букв в алфавите
    ALPHABET_SIZE = 26
    # количество рядов букв на экране
    ROWS = 2
    # количество букв в одном ряду на экране
    LETTERS_IN_ROW = ceil(ALPHABET_SIZE / ROWS)

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
            new_button.rect.center = new_button.assign_center(i % self.LETTERS_IN_ROW, i // self.LETTERS_IN_ROW)
            new_button.char = new_button.assign_char(offset=i)
            new_button.display_char()
            buttons.append(new_button)
        return buttons

    def blit_buttons(self) -> None:
        """
        Отрисовка кнопок
        """
        for button in self.buttons:
            if button.active:
                pygame.draw.circle(button.screen, button.BLACK, button.rect.center, button.radius)
                pygame.draw.circle(button.screen, button.color, button.rect.center, button.radius - button.OUTLINE)
                button.screen.blit(button.char_img, button.char_img_rect)