import os
import discord
import wikipedia
import re
import unicodedata
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

def number_words_to_numbers(number_word):
    number = {"one": 1,
              "two": 2,
              "three": 3,
              "four": 4,
              "five": 5}
    return number[number_word]

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

@bot.command(name="suggestions")
async def suggestion(ctx, input):
    embed = discord.Embed(
        title = f'Wikipedia Suggestions Results',
        colour = discord.Colour.blue()
    )
    suggestion_result = wikipedia.search(input, results = 5, suggestion=False)
    index = 1
    for suggestion in suggestion_result:
        suggestion_url = wikipedia.page(suggestion).url
        embed.add_field(name=f'{index}. {suggestion}', value='\u200b', inline=False)
        index += 1
    bot_message = await ctx.send(embed=embed)
    emoji_unicode_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
    for i in range(len(suggestion_result)):
        await bot_message.add_reaction(emoji_unicode_list[i])

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    else:
        if reaction.message.embeds:
            if reaction.message.embeds[0].title == "Wikipedia Suggestions Results":
                if reaction.emoji == "1️⃣" or reaction.emoji == "2️⃣" or reaction.emoji == "3️⃣" or reaction.emoji == "4️⃣" or reaction.emoji == "5️⃣":
                    number_word = unicodedata.name(reaction.emoji[0])
                    number_word = number_word.split(' ')[-1]
                    number = number_words_to_numbers(number_word.lower())
                    field = reaction.message.embeds[0].fields[number - 1]
                    name = field.name[3:]
                    embed = discord.Embed(
                        title = f'{name}',
                        colour = discord.Colour.blue()
                    )
                    summary = wikipedia.summary(name)
                    if len(summary) > 2048:
                        summary = summary[:2048]
                        first_occurence_white_space = len(summary)
                        for char in reversed(range(0, len(summary))):
                            if summary[char].isspace():
                                break;
                            first_occurence_white_space -= 1;
                        how_many_trailing_dots = len(summary) - first_occurence_white_space
                        summary = summary[:first_occurence_white_space - 1] + ('.')*how_many_trailing_dots
                    image_url = wikipedia.page(name).images[0]
                    embed.description = summary
                    embed.set_thumbnail(url=image_url)
                    search_result = wikipedia.search(name, results= 1, suggestion=False)
                    result_url = wikipedia.page(search_result).url
                    embed.add_field(name=search_result, value=result_url, inline=False)
                    await reaction.message.edit(embed=embed)
                    await reaction.message.clear_reactions()

                    
                    
bot.run(TOKEN)