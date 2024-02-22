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
    # максимально возможное количество ошибок
    MAX_FAULTS = 6
    # цвет для текста
    BLACK = (0, 0, 0)
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
        self.game_background = pygame.image.load('assets/background.jpg')
        self.game_background = pygame.transform.scale(self.game_background,
                                                      (self.settings.screen_width, self.settings.screen_height))
        # загаданное слово
        self.mystery_word: str = self._get_word()
        # строка для отслеживания отгадывания mystery_word
        self.guessing_word: str = "_" * len(self.mystery_word)
        # шрифт для отображения угадываемого слова
        self.guessing_font = pygame.font.Font(None, 72)
        # количество совершенных ошибок при угадывании
        self.faults: int = 0
        # класс виселицы
        self.hangtheman: HangTheMan = HangTheMan(self)
        # класс кнопок
        self.buttons_set: ButtonsSet = ButtonsSet(self)

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
                self._check_mouse_button_click(mouse_position)

    def _check_mouse_button_click(self, mouse_position) -> None:
        """
        Обработка кликов мыши
        :param mouse_position: позиция, в которой произошел клик
        """
        if self.settings.playing:
            # выбранная буква
            chosen_letter: str = ""

            for button in self.buttons_set.buttons:
                if button.rect.collidepoint(mouse_position) and button.active:
                    chosen_letter = button.char
                    button.active = False
                    break

            if chosen_letter:
                if self._is_guess_right(chosen_letter):
                    self._reveal_letter(chosen_letter)
                else:
                    self.faults += 1
        else:
            self._reset()


    def _update_window(self) -> None:
        """
        Отрисовка окна приложения
        """
        if self.settings.playing:
            self.screen.blit(self.game_background, (0, 0))
            self.hangtheman.blitme(self)
            self.buttons_set.blit_buttons()
            self._blit_guessing_word()
        else:
            ...
        pygame.display.flip()

    def _get_word(self) -> str:
        """
        Получение нового случайного слова для игры из файла со словами
        :return: слово для игры
        """
        with open(self.FILE_WITH_WORDS, 'r') as file:
            all_words: list[str] = file.readlines()
        return all_words[random.randrange(0, len(all_words) - 1)].rstrip()

    def _initiate_words(self) -> None:
        """
        Выставляет значения для загаданного слова и строки для его отгадывания
        """
        self.mystery_word = self.mystery_word = self._get_word()
        self.guessing_word = "_" * len(self.mystery_word)

    def _is_guess_right(self, letter: str) -> bool:
        """
        Проверяет, есть ли выбранная буква в слове
        :return: True, если буква в слове; False в ином случае
        """
        return letter in self.mystery_word

    def _reveal_letter(self, guessed_letter: str) -> None:
        """
        Открывает верно угаданную букву (или буквы, если буква несколько раз встречается в слове) в guessing_word
        :param guessed_letter: угаданная буква
        """
        mystery_word_list: list[str] = list(self.mystery_word)
        guessing_word_list: list[str] = list(self.guessing_word)
        indexes_of_letter: list[int] = [idx for idx, let in enumerate(mystery_word_list) if let == guessed_letter]
        for idx in indexes_of_letter:
            guessing_word_list[idx] = guessed_letter
        self.guessing_word = ''.join(guessing_word_list)

    def _blit_guessing_word(self) -> None:
        """
        Отрисовка угадываемого слова
        """
        word_img: pygame.Surface = self.guessing_font.render(self.guessing_word, True, self.BLACK)
        word_img_rect: pygame.Rect = word_img.get_rect()
        word_width: int = word_img_rect.width
        self.screen.blit(word_img, (self.settings.screen_width / 2 - word_width / 2, 400))

    def _is_game_finished(self) -> tuple[bool, str]:
        """
        Проверяет, закончена ли игра
        :return: (True, "исход"), если игра выиграна или проиграна, (False, "") в ином случае
        """
        if self.mystery_word == self.guessing_word:
            return True, "win"
        elif self.faults == self.MAX_FAULTS:
            return True, "lose"
        else:
            return False, ""

    def _reset(self) -> None:
        """
        Перезапуск игры
        """
        self.settings.playing = True
        self._initiate_words()
        self.faults = 0
        for button in self.buttons_set.buttons:
            if not button.active:
                button.active = True
