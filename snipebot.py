# bot.py
import os
import random
import discord

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

@bot.command(name='simp', help='Save to database and access from it. format command as "}simp charactername filename"')
async def simp(ctx, charactername :str, filename, save = "save"):
    
    directory = charactername
        
    # Parent Directories  
    parent_dir = "c:/Users/novalabsrobotics/Bot"
        
    # Path  
    path = os.path.join(parent_dir, directory)  
        
    # Create the directory  
    # 'charactername'  
    try:  
        os.mkdir(path) 
        print("Directory '% s' created" % directory)  
    except OSError as error:  
        print(error)   
                
    if save == "save":
        if ctx.message.attachments:
            print("save")
            await ctx.message.attachments[0].save(filename + ".png", seek_begin=True, use_cached=False)
        else:
            fmt = '{0.author}, you did not attach an object'
            print(6)
            await ctx.channel.send(fmt.format())
    elif save == "pull":
        print("pull")
        # path = os.path.join(path, filename)
        # await ctx.channel.send(os.listdir(path))
        await ctx.channel.send(file=discord.File(filename))
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