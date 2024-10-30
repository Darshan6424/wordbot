import discord
from discord.ext import commands
import requests
from utils.constants import *

class Guess(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="guess",aliases=["Guess"],description="guess command",help="command for guessing")
    async def guess(self,ctx:commands.context, word):
        print(word)
        global guesses_made,distance,GAME_NUMBER,hint
        api_url = f'https://api.contexto.me/machado/en/game/{GAME_NUMBER}/{word}'
        
        # Fetch data from the Contexto API
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                distance = data['distance']
                guessed_word = data['word']
                guesses_made += 1  # Increment the guess counter
                if distance == 0 or distance == 1:
                    await ctx.send(f'You won')
                    GAME_NUMBER+= 1
                    hint = 0
                    await ctx.send(f'New word has been chosen. Hints are now available as well')
                # Send the response to the user
                await ctx.send(f'You guessed: **{guessed_word}**\nDistance: {distance}\n')
            else:
                await ctx.send('Either u spelled it wrong or used foul word. very bad manners')
        except Exception as e:
            await ctx.send(f'An error occurred: {str(e)}')

async def setup(bot):
    await bot.add_cog(Guess(bot))
