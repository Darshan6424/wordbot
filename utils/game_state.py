class GameState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameState, cls).__new__(cls)
            cls._instance.guesses_made = 0
            cls._instance.distance = None
            cls._instance.hint_usage = {}
        return cls._instance

    def reset(self):
        self.guesses_made = 0
        self.distance = None
        self.hint_usage.clear()