from discord.ext import commands
from utils.constants import *
import random
import requests

class Hint(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="hint",aliases=["ZEUS GIVE ME A HINT AND MY LIFE IS YOURS"],description="hint command",help="gives hint to the player",hidden=false)
    async def hint(self,ctx:commands.Context,):
        global hint_usage 
        user_id = ctx.author.id

        # Initialize hint usage for the user if not already done
        if user_id not in hint_usage:
            hint_usage[user_id] = 0

        # Check if the user has exceeded the maximum number of hints
        if hint_usage[user_id] >= MAX_HINTS:
            await ctx.send(f'Sorry {ctx.author.mention}, you have used all your hints for today!')
            return



        # Check if distance is null - indicating the user has not guessed yet
        if distance is None or distance <= 0:
            await ctx.send(f'Please make a guess first before requesting a hint, {ctx.author.mention}.')
            return

        # Calculate the hint distance based on the current distance
        if distance > 200:
            # Provides a hint that is between 198 and 110
            hint_distance = random.randint(110, 198)
        elif distance >= 150:
            # Provides a hint that is between 150 and 200
            hint_distance = random.randint(150, 200)
        elif distance >= 51:
            # Provides a hint that is between 51 and 109
            hint_distance = random.randint(51, 109)
        elif distance >= 10:
            # Provides a hint that is between 10 and 50
            hint_distance = random.randint(10, 50)
        else:
            await ctx.send(f'You are too close to the answer, {ctx.author.mention}. No hint available.')
            return

        # Fetches hint from the API
        hint_api_url = f'https://api.contexto.me/machado/en/tip/{GAME_NUMBER}/{hint_distance}'

        try:
            hint_response = requests.get(hint_api_url)
            if hint_response.status_code == 200:
                hint_data = hint_response.json()
                hint_word = hint_data['word']  # the API returns a field 'word'
                await ctx.send(f'Here is your hint: **{hint_word}**\nDistance from the target word is approximately **{hint_distance}**.')
                
                # Increment the hint usage count
                hint_usage[user_id] += 1
            else:
                await ctx.send('Error fetching hint from Contexto API.')
        except Exception as e:
            await ctx.send(f'An error occurred while fetching the hint: {str(e)}')

    
async def setup(bot):
    await bot.add_cog(Hint(bot))
        
# Command to request a hint
