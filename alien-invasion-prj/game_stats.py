class GameStats:
    """ Отслеживание статистики для игры Alien Invasion. """

    def __init__(self, ai_settings):
        self.ai_setting = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """ Инициализирует статистику, изменяющуюся в ходе игры. """
        self.ships_left = self.ai_setting.ship_limit
