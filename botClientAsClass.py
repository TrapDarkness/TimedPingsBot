# bot.py
import os
import random
import discord
import requests


from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = "ODA5NTgwNDUwMzE3NzI5ODYz.YCXKjA.yEMEoEi3ByNpO_v3wZU--tgoEmI"

# 2
bot = commands.Bot(command_prefix='}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

deleted_message = "Delete?"
test_array = []
@bot.event
async def on_message_delete(message):
        fmt = '{0.author} has deleted the message: {0.content}'
        global test_message
        test_message = message
        # print(test_message)
        global test_array
        test_array.insert(0, message)
        if len(test_array) == 6:
            test_array.pop(0)
        
        print(test_array)
        await message.channel.send(fmt.format(message))

@bot.command(name='snipe', help='See deleted messages. Input command in "}snipe X" form, it will return the past X messages, up to 5')
async def snipe(ctx, depth :int):
    # fmt = '{0.author} has deleted the messages: {0.content}'
    # message_array = []
    for item in test_array[0:depth]:
        fmt = '{0.author} has deleted the message: {0.content}'
        await ctx.channel.send(fmt.format(item))

    # print(test_message)
    # await ctx.send(deleted_message)
    # print(test_array)
    # await ctx.channel.send(fmt.format(test_message))

@bot.command(name='simp', help='Access, Create and Modify folders to contain pictures of favored characters')
async def simp(msg, character :str, loc):
    # Directory 
    directory = character

    # Parent Directory path 
    parent_dir = "C:/Users/dasha/Bot"

    # Path 
    path = os.path.join(parent_dir, directory) 

    # Create the directory 
    # 'directory' in 
    # '/home / User / Documents' 
    try:  
        os.mkdir(path) 
    # print("Directory '% s' created" % directory) 
    except OSError as error:  
        print(error)

    cfg = path
    x = msg.attachments
    print(x[0])
    print(7)

    for e in msg.attachments:
        print(9)
        if e["url"].endswith(("png", "gif", "jpg")):
            print(45)
            img_data = requests.get(e["url"]).content
            sp = e["url"].split("/")
            fn = sp[len(sp) - 2] + "-" + sp[len(sp) - 1]
            with open(f"{loc}\\{fn}", "ab") as handler:
                handler.write(img_data)
                print(f"Downloaded {e['url']} to {loc}\\{fn}")
            cfg[msg.channel.id]["failsafe"] = msg.id
            cfg.save(echo=False)



bot.run(TOKEN)