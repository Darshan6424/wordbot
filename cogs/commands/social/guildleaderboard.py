import discord
from discord.ext import commands
from utils.mongo.mongo import guild_collection

class GuildLeaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="guildleaderboard",aliases=["guildtop","top_guild"], help="List the top 10 guilds by games completed")
    async def guildleaderboard(self, ctx: commands.Context):
        # Fetch the top 10 users sorted by 'games_won' in descending order
        top_guilds = guild_collection.find().sort("games_completed", -1).limit(10)
        guild_data=[]
        # Format the top users into a message
        for index, guild in enumerate(top_guilds):
            guild_data.append(f"{index + 1}. User: {(await self.bot.fetch_user(guild["id"])).name}, Games Won: {guild['games_completed']}")
        
        if guild_data:
            await ctx.send("Top 10 Guilds:\n" + "\n".join(guild_data))
        else:
            await ctx.send("No guild data found.")

# Setup function to add the cog to the bot
async def setup(bot):
    await bot.add_cog(GuildLeaderboard(bot))
