import discord
from discord.ext import commands

class fuck(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="fuck",aliases=["fucku"],description="test command",help="test command")
    async def fuck(self,ctx:commands.Context):
        await ctx.send(f"fuck off")
    
async def setup(bot):
    await bot.add_cog(fuck(bot))
        