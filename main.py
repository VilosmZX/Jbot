import random
import discord
import os 
from discord.ext import commands, tasks 
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
