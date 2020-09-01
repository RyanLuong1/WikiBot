import os
import discord
import wikipedia
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.command(name="info")
async def info(ctx, input):
    print(wikipedia.search(input))
bot.run(TOKEN)