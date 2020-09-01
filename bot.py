import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.command(name="info")
async def info(ctx, input):
    print({input})
bot.run(TOKEN)