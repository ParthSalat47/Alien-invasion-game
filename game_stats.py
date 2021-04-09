class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = False
        
        # High score should never be reset.        #Because the high score should never be reset, we initialize high_score in __init__() rather than in reset_stats().
        self.high_score = 0
    

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0      #To reset the score each time a new game starts, we initialize score in reset_stats() rather than __init__().
        self.level = 1







