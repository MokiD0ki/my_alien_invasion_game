class GameStats:
    def __init__(self, my_game):
        self.settings = my_game.settings
        self.ship_live_count = 1
        self.game_active = False
        self.score = 0

        self.stats_reset()

    def stats_reset(self):
        """Initialize the statistics"""
        self.ship_live_count = self.settings.ship_limit
        self.score = 0
