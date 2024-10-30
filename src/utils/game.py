from utils.check_new_day import check_new_day

# Function to handle daily game logic
async def daily_game_logic(bot):
    global GAME_NUMBER, guesses_made, hint_usage, yesterdays_word

    # Checks if a new day has started
    if check_new_day():
        yesterday_word = yesterdays_word  # Saves yesterday's word if needed
        
        # Increment the game number
        GAME_NUMBER += 1
        hint_usage.clear()  # Resets hint usage for all users
        guesses_made = 0  # Resets guesses for the new day
        distance = 0
        
        # Informs users about the new game
        await bot.get_channel(1296395828998701142).send(
            f'Today is a new day! The game number has increased to **{GAME_NUMBER}**.\n'
            f'Yesterday\'s word was **{yesterday_word}**.\n'
            f'Total guesses made: {guesses_made}.\n'
            f'You can now start guessing the new word!'
        )