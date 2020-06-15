class Settings:
    """ Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """ Инициализация статических настроек игры """
        # настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройка корабля
        self.ship_limit = 3

        # настройка пуль
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 5

        # настройка пришельцев
        self.fleet_drop_speed = 10

        # темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Увеличивает настройки скорости. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
