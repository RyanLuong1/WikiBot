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

def get_wikipedia_summary(input):
    return wikipedia.summary(input)

def get_wikipedia_article_images(input):
    return wikipedia.page(input).images

def get_random_wikipedia_article_image(images):
    try:
        return random.choice(images)
    except IndexError:
        return "https://cdn.discordapp.com/attachments/740004762845577297/757319155211960582/wikipedialog.png"

def create_embed_message(title = "Title"):
    embed = discord.Embed(
        title = title,
        colour = discord.Colour.blue()
    )
    return embed

def get_search_result(input):
    return wikipedia.search(input, results= 1, suggestion=False)

def get_search_result_url(search_result):
    return wikipedia.page(search_result).url

def populate_embed_message(embed, input, summary, image_url, search_result, search_result_url):
    embed.title = f'{input}'
    embed.description = summary
    embed.set_image(url=image_url)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/740004762845577297/757319155211960582/wikipedialog.png")
    embed.add_field(name=search_result, value=search_result_url, inline=False)
    return embed

def get_number_word(emoji_reaction):
    number = unicodedata.name(emoji_reaction)
    number_word = number.split(' ')[-1]
    return number_word

def get_field_from_suggestion_embed(reaction, number):
    return reaction.message.embeds[0].fields[number - 1]

def get_name_from_field(field):
    return field.name[3:]

@bot.command(name="search")
async def info(ctx, input):
    try:
        summary = get_wikipedia_summary(input)
        if len(summary) > 2048:
            summary = add_trailing_dots(summary)
        images = get_wikipedia_article_images(input)
        image_url = get_random_wikipedia_article_image(images)
        search_result = get_search_result(input)
        search_result_url = get_search_result_url(search_result)
        embed = create_embed_message()
        embed = populate_embed_message(embed, input, summary, image_url, search_result, search_result_url)
        await ctx.send(embed=embed)
    except wikipedia.DisambiguationError as error:
        possible_choices = error.options
        some_suggestions = random.sample(possible_choices, 5)
        some_suggestions_message = '\n'.join([suggestion for suggestion in some_suggestions])
        await ctx.send(f'Your input, "{input}", is too general. Please be more specific!\nTry these.\n{some_suggestions_message}')
    except wikipedia.PageError as error:
        await ctx.send(f'Your input, "{input}", does not match any pages!')

@bot.command(name="suggestions")
async def suggestion(ctx, input):
    try:
        suggestion_result = wikipedia.search(input)
        some_suggestions = random.sample(suggestion_result, 5)
        embed = create_embed_message(title = "Wikipedia Suggestions Results")
        for count, suggestion in enumerate(some_suggestions):
            embed.add_field(name=f'{count + 1}. {suggestion}', value='\u200b', inline=False)
        bot_message = await ctx.send(embed=embed)
        emoji_unicode_list = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]
        for i in range(len(some_suggestions)):
            await bot_message.add_reaction(emoji_unicode_list[i])
    except wikipedia.DisambiguationError as error:
        possible_choices = error.options
        some_suggestions = random.sample(possible_choices, 5)
        some_suggestions_message = '\n'.join([suggestion for suggestion in some_suggestions])
        await ctx.send(f'Your input, "{input}", is too general. Please be more specific!\nTry these.\n{some_suggestions_message}')
    except wikipedia.PageError as error:
        await ctx.send(f'Your input, "{input}", does not match any pages!')

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    else:
        if reaction.message.embeds:
            if reaction.message.embeds[0].title == "Wikipedia Suggestions Results":
                if reaction.emoji == "1️⃣" or reaction.emoji == "2️⃣" or reaction.emoji == "3️⃣" or reaction.emoji == "4️⃣" or reaction.emoji == "5️⃣":
                    number_word = get_number_word(reaction.emoji[0])
                    number = number_words_to_numbers(number_word.lower())
                    field = get_field_from_suggestion_embed(reaction, number)
                    name = get_name_from_field(field)
                    summary = wikipedia.summary(name)
                    if len(summary) > 2048:
                        summary = add_trailing_dots(summary)
                    images = get_wikipedia_article_images(name)
                    image_url = get_random_wikipedia_article_image(images)
                    search_result = get_search_result(name)
                    search_result_url = get_search_result_url(search_result)
                    embed = create_embed_message()
                    embed = populate_embed_message(embed, name, summary, image_url, search_result, search_result_url)
                    await reaction.message.edit(embed=embed)
                    await reaction.message.clear_reactions()

                    
                    
bot.run(TOKEN)