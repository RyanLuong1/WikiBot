import os
import discord
import wikipedia
import re
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.command(name="info")
async def info(ctx, input):
    embed = discord.Embed(
        title = f'{input}',
        colour = discord.Colour.blue()
    )
    summary = wikipedia.summary(input)
    if len(summary) > 2048:
        summary = summary[:2048]
        first_occurence_white_space = len(summary)
        for char in reversed(range(0, len(summary))):
            if summary[char].isspace():
                break;
            first_occurence_white_space -= 1;
        how_many_trailing_dots = len(summary) - first_occurence_white_space
        summary = summary[:first_occurence_white_space - 1] + ('.')*how_many_trailing_dots
    image_url = wikipedia.page(input).images[0]
    embed.description = summary
    embed.set_thumbnail(url=image_url)
    search_result = wikipedia.search(input, results= 1, suggestion=False)
    result_url = wikipedia.page(search_result).url
    embed.add_field(name=search_result, value=result_url, inline=False)
    await ctx.send(embed=embed)

@bot.command(name="suggestion")
async def suggestion(ctx, input):
    embed = discord.Embed(
        title = f'{input}',
        colour = discord.Colour.blue()
    )
    suggestion_result = wikipedia.search(input, results = 5, suggestion=False)
    index = 1
    for suggestion in suggestion_result:
        suggestion_url = wikipedia.page(suggestion).url
        embed.add_field(name=f'{index}. {suggestion}', value='\u200b', inline=False)
        index += 1
    await ctx.send(embed=embed)
bot.run(TOKEN)