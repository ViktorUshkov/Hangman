import os
import pygame

class HangTheMan:
    """
    Класс виселицы
    """
    # директория с ассетами виселицы
    HANGMAN_ASSETS_PATH = "assets/hangman/"
    def __init__(self, hangman):
        """
        Инициализация класса
        :param hangman: экземпляр основного класса игры Hangman
        """
        self.screen = hangman.screen
        self.screen_rect = hangman.screen.get_rect()
        # ассеты для виселицы
        self.assets = self._load_assets()
        self.rect = None

    def blitme(self, hangman) -> None:
        """
        Отрисовка виселицы: рисуем такой по порядку ассет, сколько ошибок совершил игрок
        :param hangman: экземпляр основного класса игры Hangman (для информации об ошибках игрока)
        """
        hang_stage = self.assets[hangman.faults]
        self.rect = hang_stage.get_rect()
        self.rect.midtop = (self.screen_rect.midtop[0], self.screen_rect.midtop[1] + 100)
        self.screen.blit(hang_stage, self.rect)

    def _load_assets(self) -> list[pygame.Surface]:
        """
        Загрузка ассетов для виселицы из директории self.HANGMAN_ASSETS_PATH
        :return: упорядоченный по этапам список с ассетами виселицы
        """
        assets = []
        for asset_name in sorted(os.listdir(self.HANGMAN_ASSETS_PATH)):
            asset = pygame.image.load(self.HANGMAN_ASSETS_PATH + asset_name).convert()
            asset.set_colorkey((255, 255, 255))
            assets.append(asset)
        return assets


