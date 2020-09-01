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
    embed = discord.Embed(
        title = f'Search Results',
        description = f'Here are the results of searching for {input}....',
        colour = discord.Colour.blue()
    )
    search_results = wikipedia.search(input, results= 10, suggestion=True)
    for result in search_results:
        result_url = wikipedia.page(result).url
        embed.add_field(name=result, value=result_url, inline=False)
    await ctx.send(embed=embed)
bot.run(TOKEN)