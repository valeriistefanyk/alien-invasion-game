class Settings:
    """ Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """ Инициализация настроек игры """
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3
