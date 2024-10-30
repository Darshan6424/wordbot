import discord
from discord.ext import commands
from utils.mongo.mongo import user_collection

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="leaderboard",aliases=["top","top_users"], help="List the top 10 users by games won")
    async def leaderboard(self, ctx: commands.Context):
        # Fetch the top 10 users sorted by 'games_won' in descending order
        top_users = user_collection.find().sort("games_won", -1).limit(10)
        users_data=[]
        # Format the top users into a message
        for index, user in enumerate(top_users):
            users_data.append(f"{index + 1}. User: {(await self.bot.fetch_user(user["id"])).name}, Games Won: {user['games_won']}")
        
        if users_data:
            await ctx.send("Top 10 Users:\n" + "\n".join(users_data))
        else:
            await ctx.send("No user data found.")

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
