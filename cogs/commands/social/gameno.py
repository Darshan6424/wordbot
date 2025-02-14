import discord
from discord.ext import commands
from utils.mongo.mongo import guild_collection
from utils.constants import MIN_GAME_NUMBER,MAX_GAME_NUMBER
import random

class GameNo(commands.Cog):
    def __init__(self,bot):
        self.bot=bot;
    @commands.hybrid_command(name="gameno",aliases=["gamenumber"],description="gives game number",help="commands for giving game number")
    async def gameno(self,ctx:commands.context):
        guildInfo = guild_collection.find_one({"id":ctx.guild.id})
        if guildInfo is None:
            gameNumber = random.randint(MIN_GAME_NUMBER,MAX_GAME_NUMBER)
            guild_collection.insert_one({"id": ctx.guild.id, "current_game_no": gameNumber, "games_completed": 0})

        else:
            gameNumber = guildInfo["current_game_no"]
        
        await ctx.reply(f"The game number that is running in the guild is {gameNumber}.")

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(GameNo(bot))