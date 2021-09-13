# WikiBot

<div align="center">

![wikibot-01](https://user-images.githubusercontent.com/47546985/131376133-50686d05-495c-4321-b6f8-6ffa0e579808.jpg)

[![made-with-discord.py](https://img.shields.io/badge/Made%20with-Discord.py-orange)](https://discordpy.readthedocs.io/en/latest/)
[![GitHub](https://img.shields.io/github/license/RyanLuong1/Moji)](https://github.com/RyanLuong1/WikiBot/blob/master/LICENSE)

</div>
</br>

## Table of Contents
* [Description](https://github.com/RyanLuong1/WikiBot#description)
* [Commands](https://github.com/RyanLuong1/WikiBot#commands)
* [Commands Usage](https://github.com/RyanLuong1/WikiBot#commands-usage)
* [Setup](https://github.com/RyanLuong1/WikiBot#setup)
   * [Prerequistes for Linux](https://github.com/RyanLuong1/WikiBot#prerequistes-for-linux)
      * [Installing Prerequistes](https://github.com/RyanLuong1/WikiBot#installing-prerequistes)
   * [Prerequistes for Windows 10](https://github.com/RyanLuong1/WikiBot#prerequistes-for-windows-10)
      * [Installing Prerequistes](https://github.com/RyanLuong1/WikiBot#installing-prerequistes-1)
   * [Discord Bot Setup](https://github.com/RyanLuong1/WikiBot#discord-bot-setup)
   * [WikiBot Setup (Linux)](https://github.com/RyanLuong1/WikiBot#wikibot-setup-linux)
      * [Running Moji](https://github.com/RyanLuong1/WikiBot#running-wikibot)
   * [Moji Setup (Windows 10)](https://github.com/RyanLuong1/WikiBot#wikibot-setup-windows-10)
      * [Running Moji](https://github.com/RyanLuong1/WikiBot#running-wikibot-1)
* [Troubleshooting (Linux)](https://github.com/RyanLuong1/WikiBot#troubleshooting-linux)
* [Troubleshooting (Windows 10)](https://github.com/RyanLuong1/WikiBot#troubleshooting-windows-10)
* [Contact](https://github.com/RyanLuong1/WikiBot#contact)

## Description

WikiBot is a self hosting Discord bot which allows users to search up any Wikipedia articles.

<div align="center">

![wikibot_gif](https://user-images.githubusercontent.com/47546985/131381693-a3a5dbc2-7531-4214-a76a-123b440f3227.gif)

![wikibot_gif_suggestions](https://user-images.githubusercontent.com/47546985/131396776-e0087046-0b6e-4ff4-8020-3e6f1f245550.gif)

</div>
</br>

## Commands
Prefix: !

</br>

## Commands Usage
*   !search "\<input>"
     Find one Wikipedia article and display the title, summary, link, and picture in an embed message.
</br>

*   !suggestions "\<input>"
     Find up to five Wikipedia articles and display the name in an embed message. The embed message will have reactions that the user can react to. The embed message will display the title, summary, link, and the article's picture based on the number.
</br>

> The user must enter quotes. If not, any words after the space of the input will not be considered 

> A picture will only be in the embed message if the article contains it

## Installation

### Prerequistes for Linux
* [Python 3.6 or higher](https://www.python.org/downloads/)
* [discord.py](https://github.com/Rapptz/discord.py)

#### Installing Prerequistes

##### Terminal
```
sudo apt-get update
sudo apt-get install python3.6
python3 -m pip install -U discord.py
```

>First two steps are only required if you do not have ≥python 3.6 installed

>You don't have to get python 3.6, but any version you install must be 3.6 or higher. If you get python 3.7, then it would be ```sudo apt-get install python3.7``` 

>Press enter for each command you type

### Prerequistes for Windows 10
* [Python 3.6 or higher](https://www.python.org/downloads/)
* [discord.py](https://github.com/Rapptz/discord.py)
* [Git](https://git-scm.com/downloads)

#### Installing Prerequistes for Windows 10

1. Download the executable on [Python.org](https://www.python.org/downloads/)
2. Download Git on the [Git page](https://git-scm.com/downloads)

>Mark sure to tick the ```Add Python # to PATH``` box for the Python installer

>Leave everything default for the Git installer

##### Command Prompt
```
py -3 -m pip install -U discord.py
python -m pip install pymongo
```

>Press enter for each command you type

## Setup
Setting up WikiBot requires yourself to host it.


### Discord Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers). 
2. Login using your existing Discord account or create one if you don't have one.
3. Click the ```New Application``` button.
4. Name your ```Application``` and click ```Create```
5. On the left panel, click ```Bot``` and click the ```Add Bot``` button
6. On the left panel, click ```OAuth2```
7. Check ```bot``` under ```scopes```.
8. Under ```Bot Permissions```, check ```Manage Emojis```, ```Send Messages```, ```Manage Messages```, ```Use External Emojis```, and ```Add Reactions```.
9. Copy and paste the URL generated under ```scopes```, select your guild and click ```Authorize```. Check that your bot is in your guild. It should be offline.
10. Click ```Bot``` on the left panel and click either the ```Copy``` button or ```Click to Reveal Token``` to get your bot token.

### WikiBot Setup (Linux)
1. Open terminal and type ```git clone https://github.com/RyanLuong1/Wikibot.git```
2. Change your directory to the bot directory ```cd /WikiBot``` and type ```pip3 install -r requirements.txt```.
3. In the same directory, create a new file ```.env``` by typing ```touch .env``` and opening it through the terminal or through your preferred text editor. It should contain the following:
   ```
     DISCORD_TOKEN= "YOUR_DISCORD_TOKEN"
   ```
4. Replace ```"YOUR_DISCORD_TOKEN"``` with their respective token

>```DISCORD_TOKEN``` is from step 10 of ```Discord Bot Setup```


#### Running WikiBot
1. Go to the bot directory and type ```python3 bot.py```. Now you are able to search up any Wikipedia articles


### WikiBot Setup (Windows 10)
1. Open command prompt and type ```cd Downloads```
2. Type ```git clone https://github.com/RyanLuong1/WikiBot.git``` 
3. Type ```cd WikiBot``` and type ```pip3 install -r requirements.txt```
4. In the same directory, create a new file ```.env``` by typing ```type nul > .env``` and opening through the command prompt or through your preferred text editor. It should contain the following:
    ```
      DISCORD_TOKEN = "YOUR_DISCORD_TOKEN"
    ```
5. Replace your ```"YOUR_DISCORD_TOKEN"``` and ```"YOUR_CONNECTION_STRING"``` with their respective token and connection string.
</br>

>```DISCORD_TOKEN``` is from step 10 of ```Discord Bot Setup```

#### Running WikiBot
1. Go to the bot directory and type ```python bot.py```. Now you can search up any Wikipedia articles.

## Troubleshooting (Linux)

```TypeError: __new__() got an unexpected keyword argument 'deny_new'```

[Solution](https://stackoverflow.com/questions/63027848/discord-py-glitch-or-random-error-typeerror-new-got-an-unexpected-keywor). Discord most likely have updated discord.py. Type ```python3 -m pip install -U discord.py```

```TypeError: __init__() got an unexpected keyword argument 'requote'```

[Solution](https://github.com/Rapptz/discord.py/issues/5162). Read Rapptz's response. Type ```pip3 install -U yarl==1.4.2```

## Contact
* Discord: ```Ryаn#6513``` 
