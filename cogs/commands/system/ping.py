import discord
from discord.ext import commands

class Ping(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="ping",aliases=["latency"],description="ping command",help="Displays the bot's latency to the server.")
    async def ping(self,ctx:commands.Context):
        await ctx.send(f"pong, latency:{round(self.bot.latency*1000)}ms")
    
async def setup(bot):
    await bot.add_cog(Ping(bot))
        