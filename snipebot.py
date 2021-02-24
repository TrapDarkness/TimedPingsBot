# bot.py
import os
import random
import discord
from discord import file

from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = "INSERT_TOKEN_HERE"

# 2
bot = commands.Bot(command_prefix='}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice. Input in form "roll_dice X Y" X is number of dice to be rolled, and Y is the number of sides on those dice. Max is 69')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_dice > 69:
        number_of_dice = 69
    if number_of_sides > 69:
        number_of_sides = 69
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

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
        # await message.channel.send(fmt.format(message))

# @bot.event
# async def on_message(message):
#         if message.attachments:
#             print(5)
#             await message.attachments[0].save("Weiss.png", seek_begin=True, use_cached=False)

#         global test_message
#         test_message = message
#         # print(test_message)
#         global test_array
#         test_array.insert(0, message)
#         if len(test_array) == 6:
#             test_array.pop(0)
        
#         print(test_array)
#         # await message.channel.send(fmt.format(message))

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

@bot.command(name='simp', help='Save to database and access from it. format command as "}simp charactername filename save" where save can be either save or pull, depending on if one wants to save the image or pull it from the database. Filename is the desired name of the file when saved, not what the file is currently called on your device. Charactername is the name of the character or ship. make sure the file is attached to the same message as the command not sent in separate ones')
async def simp(ctx, charactername :str, filename, save = "save"):
    guild = ctx.message.guild.name
    directory = charactername
        
    # Parent Directories  
    parent_dir = "c:/Users/novalabsrobotics/Bot/"
    parent_dir += guild

    # Path  
    path = os.path.join(parent_dir, directory)  
        
    # Create the directory  
    # 'charactername'  
    try:  
        os.mkdir(parent_dir) 
        print("Directory '% s' created for server" % directory)  
    except OSError as error:  
        print(error)   

    try:  
        os.mkdir(path) 
        print("Directory '% s' created for character" % directory)  
    except OSError as error:  
        print(error)   
                
    if save == "save":
        if ctx.message.attachments:
            print("save")
            path_file = os.path.join(parent_dir, charactername, filename)  
            print(path_file)
            path_dir = os.listdir(path)
            print(path_dir)
            filename_png = filename + ".png"
            if filename_png in path_dir:
                fmt = 'That filename already exists, please choose a different name'
                print("file already exists")
                await ctx.channel.send(fmt)
            else:
                await ctx.message.attachments[0].save(path_file + ".png", seek_begin=True, use_cached=False)
        else:
            fmt = '{0.author}, you did not attach an object'
            print(6)
            await ctx.channel.send(fmt.format())
    elif save == "pull":
        print("pull")
        filename += ".png"
        print(filename)
        flags = os.O_RDWR | os.O_CREAT 

        # path = os.path.join(path, filename)
        # await ctx.channel.send(os.listdir(path))
        path_file = os.path.join(parent_dir, charactername, filename)  
        print(path_file)
        # await ctx.channel.send(os.open(path1, flags))

        await ctx.channel.send(file=discord.File(path_file))

        # await ctx.channel.send(file=discord.File(filename))

        # with open(parent_dir, 'rb') as fp:
        #     await ctx.channel.send(file=discord.File(fp, filename))

    else:
        fmt = 'You did not input correct save'
        print('wrong save form')
        await ctx.channel.send(fmt)
    # if ctx.message.attachments:
    #     print(5)
    #     await ctx.message.attachments[0].save("newtesting.png", seek_begin=True, use_cached=False)

    


    

bot.run(TOKEN)