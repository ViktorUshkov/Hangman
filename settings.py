class Settings:
    """
    Класс настроек приложения
    """
    # ширина экрана
    SCREEN_WIDTH = 800
    # высота экрана
    SCREEN_HEIGHT = 800

    def __init__(self):
        """
        Инициализация класса настроек
        """
        self.screen_width = self.SCREEN_WIDTH
        self.screen_height = self.SCREEN_HEIGHT
        # показывает, идёт ли в данный момент игра
        self.playing = True