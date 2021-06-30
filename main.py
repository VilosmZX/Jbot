import random
import discord
import os 
from discord.ext import commands, tasks
from discord.ext.commands import cooldowns
from discord.ext.commands.core import cooldown
from discord.ext.commands.errors import BadArgument, CommandOnCooldown, MissingPermissions 
import dotenv 

dotenv.load_dotenv()
bot = commands.Bot(command_prefix='-')
TOKEN = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready")

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return 
    
@bot.event 
async def on_command_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.reply("```Missing permissions ❌ ```")
    elif isinstance(error, BadArgument):
        await ctx.reply("```Missing arguments ❌```")
    elif isinstance(error, CommandOnCooldown):
        ctx.reply(f"```Please wait for a few seconds before using this command again ❌```")

if __name__ == '__main__':
    for command in os.listdir('./cogs'):
        if command.endswith('.py'):
            try:
                ext = command[:-3]
                bot.load_extension(f"cogs.{ext}")
                print(f"{ext} has been loaded.")
            except Exception as error:
                print(f"ERROR: {error}".upper())


bot.run(TOKEN)
