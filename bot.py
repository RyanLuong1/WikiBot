import os
import discord
import wikipedia
import re
import unicodedata
import random
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

def add_trailing_dots(summary):
    summary = summary[:2048]
    white_space_occurence = len(summary)
    first_white_space_found = False
    for char in reversed(range(0, len(summary))):
        if summary[char].isspace():
            if not first_white_space_found:
                first_white_space_found = True
            else:
                break;
        white_space_occurence -= 1;
    how_many_trailing_dots = len(summary) - white_space_occurence
    summary = summary[:white_space_occurence - 1] + ('.')*how_many_trailing_dots
    return summary

def get_wikipedia_article_images(input):
    return wikipedia.page(input).images

def get_random_wikipedia_article_image(images):
    return random.choice(images)

def create_embed_message():
    embed = discord.Embed(
        title = f'Title',
        colour = discord.Colour.blue()
    )
    return embed

@bot.command(name="search")
async def info(ctx, input):
    try:
        summary = wikipedia.summary(input)
        if len(summary) > 2048:
            summary = add_trailing_dots(summary)
        images = get_wikipedia_article_images(input)
        image_url = get_random_wikipedia_article_image(images)
        embed = create_embed_message()
        embed.description = summary
        embed.set_image(url=image_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740004762845577297/757319155211960582/wikipedialog.png")
        search_result = wikipedia.search(input, results= 1, suggestion=False)
        result_url = wikipedia.page(search_result).url
        embed.add_field(name=search_result, value=result_url, inline=False)
        await ctx.send(embed=embed)
    except wikipedia.DisambiguationError:
        await ctx.send(f'Your input, "{input}", is too general. Please be more specific!')

@bot.command(name="suggestions")
async def suggestion(ctx, input):
    try:
        suggestion_result = wikipedia.search(input, results = 5, suggestion=False)
        embed = discord.Embed(
            title = f'Wikipedia Suggestions Results',
            colour = discord.Colour.blue()
        )
        index = 1
        for suggestion in suggestion_result:
            suggestion_url = wikipedia.page(suggestion).url
            embed.add_field(name=f'{index}. {suggestion}', value='\u200b', inline=False)
            index += 1
        bot_message = await ctx.send(embed=embed)
        emoji_unicode_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
        for i in range(len(suggestion_result)):
            await bot_message.add_reaction(emoji_unicode_list[i])
    except wikipedia.DisambiguationError:
        await ctx.send(f'Your input, "{input}", is too general. Please be more specific!')

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
                        white_space_occurence = len(summary)
                        for char in reversed(range(0, len(summary))):
                            if summary[char].isspace():
                                break;
                            white_space_occurence -= 1;
                        how_many_trailing_dots = len(summary) - white_space_occurence
                        summary = summary[:white_space_occurence - 1] + ('.')*how_many_trailing_dots
                    image = wikipedia.page(name).images
                    image_url = random.choice(image)
                    embed.description = summary
                    embed.set_image(url=image_url)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740004762845577297/757319155211960582/wikipedialog.png")
                    search_result = wikipedia.search(name, results= 1, suggestion=False)
                    result_url = wikipedia.page(search_result).url
                    embed.add_field(name=search_result, value=result_url, inline=False)
                    await reaction.message.edit(embed=embed)
                    await reaction.message.clear_reactions()

                    
                    
bot.run(TOKEN)