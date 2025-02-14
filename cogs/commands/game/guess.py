import discord
from discord.ext import commands
import requests
from utils.constants import MIN_GAME_NUMBER,MAX_GAME_NUMBER
from utils.mongo.mongo import guild_collection,user_collection
import random
from utils.mongo.schema.guild_schema import Guild_schema
from utils.game_state import GameState
class Guess(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        self.game_state=GameState()
        
    @commands.hybrid_command(name="guess",aliases=["Guess"],description="guess command",help="command for guessing")
    async def guess(self,ctx:commands.context, word):
        guildInfo = guild_collection.find_one({"id":ctx.guild.id})
        if guildInfo is None:
            GAME_NUMBER = random.randint(MIN_GAME_NUMBER,MAX_GAME_NUMBER)
            
            guild_collection.insert_one({"id": ctx.guild.id, "current_game_no": GAME_NUMBER, "games_completed": 0})

        else:
            GAME_NUMBER = guildInfo["current_game_no"]
        
        api_url = f'https://api.contexto.me/machado/en/game/{GAME_NUMBER}/{word}'
        
        # Fetch data from the Contexto API
        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                self.game_state.distance = data['distance']
                guessed_word = data['word']
                self.game_state.guesses_made += 1  # Increment the guess counter
                user_collection.update_one(
                            {"id":ctx.author.id},
                            {
                                "$inc":{
                                    "total_guesses":1
                                }
                            },upsert=True
                        )
                
                if self.game_state.distance == 0 or self.game_state.distance == 1:
                    await ctx.send(f'You won')
                    self.game_state.hint_usage.clear()
                    self.game_state.guesses_made=0
                    self.game_state.distance=None
                    newGameNumber=GAME_NUMBER+1
                    
                    if newGameNumber>MAX_GAME_NUMBER:
                        guild_collection.update_one(
                            {"id":ctx.guild.id},
                            {
                                "$set":{
                                    "current_game_no":random.randint(MIN_GAME_NUMBER,MAX_GAME_NUMBER)
                                }
                            },upsert=True
                        )
                    else:
                        guild_collection.update_one(
                            {"id":ctx.guild.id},
                            {
                                "$set":{
                                    "current_game_no":newGameNumber
                                }
                            },upsert=True
                        )
                    await ctx.send(f'New word has been chosen. Hints are now available as well')
                # Send the response to the user
                await ctx.send(f'You guessed: **{guessed_word}**\nDistance: {self.game_state.distance}\n')
            else:
                await ctx.send('Either u spelled it wrong or used foul word. very bad manners')
        except Exception as e:
            await ctx.send(f'An error occurred: {str(e)}')

async def setup(bot):
    await bot.add_cog(Guess(bot))
