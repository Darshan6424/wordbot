import discord
from discord.ext import commands, tasks
import datetime
from utils.constants import *
from utils.mongo.mongo import guild_collection
import random
from utils.game_state import GameState

class DailyReset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_reset.start()  
        self.game_state=GameState()

    @tasks.loop(hours=24)  
    async def daily_reset(self):
        global guesses_made,distance
            # Increment the game number
        self.game_state.hint_usage.clear()
        self.game_state.guesses_made=0
        self.game_state.distance=None
        
        guilds=guild_collection.find()
        for guild in guilds:
            GAME_NUMBER =guild["current_game_no"]
            newGameNumber=GAME_NUMBER+1
            if newGameNumber>MAX_GAME_NUMBER:
                guild_collection.update_one(
                    {"id":guild["id"]},
                    {
                        "$set":{
                            "current_game_no":random.randint(MIN_GAME_NUMBER,MAX_GAME_NUMBER)
                        }
                    },upsert=True
                )
            else:
                guild_collection.update_one(
                    {"id":guild["id"]},
                    {
                        "$set":{
                            "current_game_no":newGameNumber
                        }
                    },upsert=True
                )
        
        # Informs users about the new game
        await self.bot.get_channel(1296395828998701142).send(
            f'Today is a new day!'
            f'The game has been reset'
            f'You can now start guessing the new word!'
        )

    @daily_reset.before_loop
    async def before_daily_reset(self):
        # Wait until the time you want the message to be sent
        target_time = datetime.time(hour=0, minute=0)  # Set the desired time (e.g., 12 AM)
        now = datetime.datetime.now()
        # Calculate the seconds until the next occurrence of target_time
        next_run = datetime.datetime.combine(now.date(), target_time)
        if now.time() > target_time:
            next_run += datetime.timedelta(days=1)  # Schedule for the next day if the time has already passed
        await discord.utils.sleep_until(next_run)  # Sleep until the target time

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(DailyReset(bot))
