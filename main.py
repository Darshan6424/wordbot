import asyncio
import discord
from discord.ext import commands
from datetime import datetime  
from dotenv import load_dotenv
import os

from keep_alive import keep_alive
from utils.constants import *
from utils.cogs_loader import load_cogs
from utils.mongo.mongo import create_db

load_dotenv()

create_db()
keep_alive()

intents = discord.Intents.all()
intents.members=True
intents.message_content = True  # Enable the intent for message content

# Create the bot with the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event when the bot is ready

async def main():
    async with bot:
        try:
            await load_cogs(bot)
            # run the bot with your token
            
            await bot.start(os.environ['discord_token'])
            # await daily_game_logic()
        except Exception as e:
            print(f"Error starting bot: {e}")

asyncio.run(main())
