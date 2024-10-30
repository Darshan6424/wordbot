# Command to provide help and tips
import discord
from discord.ext import commands

class Guide(commands.Cog):   
    def __init__(self,bot):
        self.bot=bot
        
    @commands.hybrid_command(name="guide",aliases=["tf do i do","tf"],description="guide command",help="Displays the guide to the game")
    async def guide(self,ctx:commands.Context):
        guide_message = (
            "Welcome to the Guess the word Game!\n\n"
            "**How to Play:**\n"
            "1. The game starts with a secret word that you must guess.\n"
            "2. Use the `!guess <your_word>` command to make a guess.\n"
            "3. After each guess, you'll receive feedback on how far away your guess is from the secret word.\n"
            "4. You can also use the `!hint` command to receive a hint about the word.\n\n"
            "**Tips for Playing:**\n"
            "- Start with common words to get a sense of the distance.\n"
            "- Pay attention to the distance feedback to narrow down your guesses.\n"
            "- Use hints wisely; you have a limited number of hints available per day.\n"
            "- Keep track of your previous guesses to avoid repeating them.\n\n"
            "Have fun, and good luck guessing the word!"
        )
        
        await ctx.send(guide_message)
        
    
async def setup(bot):
    await bot.add_cog(Guide(bot))
        
