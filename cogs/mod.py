import discord
from discord.ext import commands 
import datetime

timestamp = datetime.datetime.now()
time_now = timestamp.strftime(r"%I:%M %p")

class Mod(commands.Cog):
   def __init__(self, bot):
      self.bot = bot 
      
   # Command starts from here 
   @commands.command(name='purge')
   @commands.has_permissions(manage_messages=True)
   async def purge(self, ctx, amount : int = 0):
      if amount == 0:
         return 
      else:
         await ctx.channel.purge(limit=amount)
         embed = discord.Embed(
            title = f"{amount} message has been cleared",
            color = discord.Color.green()
         )
         embed.set_footer(icon=ctx.author.icon_url, text=f"Command executed by {ctx.author.mention}  |  Today at {time_now}")
         
def setup(bot):
   bot.add_cog(Mod(bot))
        
