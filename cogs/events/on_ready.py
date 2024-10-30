import discord
from discord.ext import commands
from utils.config import DEV_SERVERS,DEV

class OnReady(commands.Cog):   
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
         # Sync commands for all specified test servers
        if DEV:
            for server_id in DEV_SERVERS:
                try:
                    await self.bot.tree.sync(guild=discord.Object(id=server_id))
                    print(f"Successfully synced application command tree for guild {server_id}")
                except Exception as e:
                    print(f"Failed to sync for guild {server_id}: {e}")
        else:
            try:
                await self.bot.tree.sync()
                print(f"Successfully synced application command tree for every guild")
            except Exception as e:
                    print(f"Failed to sync for servers: {e}")
                    
        print("synced the application command tree")
        print(f"the bot {self.bot.user} is online")
        
        
async def setup(bot):
    await bot.add_cog(OnReady(bot))
