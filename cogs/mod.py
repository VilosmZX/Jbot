import discord
from discord.ext import commands 
import datetime

timestamp = datetime.datetime.now()
time_now = timestamp.strftime(r"%I:%M %p")
class Mod(commands.Cog):
    def _init__(self, bot):
        self.bot = bot 

    @commands.command(name='kick')
    @commands.has_permissions(kick_members = True)
    @commands.cooldown(rate=1, per=60)
    async def kick(self, ctx, target : discord.Member = None, *, reason : str = None):
        if reason is None:
            reason = "no reason"

        if target is None:
            await ctx.reply("```Masukan target!```")

        if target != None and reason != None:
            await target.kick(reason=reason)
            embed = discord.Embed(
                title = f"Kick Berhasil!",
                color = ctx.author.color
            )
            embed.add_field(name='<< Target >> ', value=f"{target.mention}")
            embed.add_field(name='<< Alasan >>  ', value=f"{reason}")
            embed.set_footer(icon_url=ctx.author.icon_url, text=f"Kicked by {ctx.author}  |  Today at {time_now}")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mod(bot))
        
