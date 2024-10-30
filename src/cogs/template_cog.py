import discord
from discord.ext import commands

class Template_cog(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="template",aliases=["template-alias1","template-alias2"],description="command template for cogs",help="what is going to be shown in the default help meneu",hidden=True)
    async def template(self,ctx:commands.Context,*,args:str=None):
        await ctx.reply("just a template command nothing else")
    
async def setup(bot):
    await bot.add_cog(Template_cog(bot))
        