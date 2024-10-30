import datetime
# Constants
GAME_NUMBER = 300  # Initial game number
MAX_HINTS = 3  # Maximum number of hints per day
hint_usage = {}  # Track hint usage by user
guesses_made = 0  # Track total guesses made
yesterdays_word = ''  # Store yesterday's word
distance = None
current_date=datetime.datetime.now()