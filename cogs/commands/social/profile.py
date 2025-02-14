import discord
from discord.ext import commands
from utils.mongo.mongo import user_collection

class Profile(commands.Cog):
    def __init__(self,bot):
        self.bot=bot;
    @commands.hybrid_command(name="profile",aliases=["my"],description="to display the user profile",help="displays the user the profile")
    async def profile(self,ctx:commands.context):
        userInfo = user_collection.find_one({"id":ctx.author.id})
        if userInfo is None:
            user_collection.insert_one({"id": ctx.author.id, "games_won":0,"total_guesses":0,"total_hint_used":0})
            games_won=0
            total_guesses=0
            total_hint_used=0
        else:
            games_won=userInfo["games_won"]
            total_guesses=userInfo["total_guesses"]
            total_hint_used=userInfo["total_hint_used"]
        
        await ctx.send(f"user: {ctx.author.name}\ngames won: {games_won}\ntotal guesses: {total_guesses}\ntotal hint used: {total_hint_used}")

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(Profile(bot))