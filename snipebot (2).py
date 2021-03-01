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
edited_message_before = "Edited Before?"
edited_before_array = []
edited_message_after = "Edited After??"
edited_after_array = []
@bot.event
async def on_message_delete(message):
        fmt = '{0.author} has deleted the message: {0.content}'
        global test_message
        test_message = message
        # print(test_message)
        
        global test_array
        if len(test_array) == 6:
            test_array.pop(0)
        test_array.insert(0, message)
        
        
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
@bot.event
async def on_message_edit(message_before, message_after):
    


    global edited_message_before
    edited_message_before = message_before
    global edited_message_after
    edited_message_after = message_after

    # print(test_message)
    global edited_before_array
    if len(edited_before_array) == 6:
        edited_before_array.pop(0)
    edited_before_array.insert(0, edited_message_before)


    global edited_after_array
    if len(edited_after_array) == 6:
        edited_after_array.pop(0)
    edited_after_array.insert(0, edited_message_after)


    print(edited_after_array[0].content)


@bot.command(name='snipe', help='See deleted messages. Input command in "}snipe X" form, it will return the past X messages, up to 5')
async def snipe(ctx, depth :int):
    # fmt = '{0.author} has deleted the messages: {0.content}'
    # message_array = []
    for item in test_array[0:depth]:
        fmt = '{0.author} has deleted the message: {0.content}'
        await ctx.channel.send(fmt.format(item))

@bot.command(name='editsnipe', help='See edited messages. Input command in "}editsnipe X" form, it will return the past X messages, up to 5')
async def editsnipe(ctx, depth :int):
    # fmt = '{0.author} has deleted the messages: {0.content}'
    # message_array = []
    i = 0
    for item in edited_after_array[0:depth]:
        if edited_after_array[0].guild.name == ctx.guild.name:
            fmt = str(edited_before_array[i].author) + ' has edited their message from: "' + edited_before_array[i].content + '" to: "' + edited_after_array[i].content + '" in ' + str(edited_after_array[i].channel)
            await ctx.channel.send(fmt)
            i += 1

    # print(test_message)
    # await ctx.send(deleted_message)
    # print(test_array)
    # await ctx.channel.send(fmt.format(test_message))

@bot.command(name='simp', help='Save to database and access from it. format command as "}simp charactername filename save" where save can be either save or pull, depending on if one wants to save the image or pull it from the database. Filename is the desired name of the file when saved, not what the file is currently called on your device. Charactername is the name of the character or ship. make sure the file is attached to the same message as the command not sent in separate ones')
async def simp(ctx, charactername :str, filename, save = "save"):
    guild = ctx.message.guild.name
    directory = charactername
        
    # Parent Directories  
    # parent_dir = "c:/Users/novalabsrobotics/Bot/"
    parent_dir = "c:/Users/dasha/Bot/"
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
                fmt = 'File Succesfully Saved!'
                print("file saved")
                await ctx.message.attachments[0].save(path_file + ".png", seek_begin=True, use_cached=False)
                await ctx.channel.send(fmt)
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
    elif save == "delete":
        if "moderator" in [i.name.lower() for i in ctx.author.roles]:
            print("delete")
            filename += ".png"

            path_file = os.path.join(parent_dir, charactername, filename)  
            print(path_file)
            path_dir = os.listdir(path)
            print(path_dir)
            os.remove(path_file)

            fmt = 'File Deleted'
            print('file deleted')
            await ctx.channel.send(fmt)

        # Do things only moderators can do
        else:
            fmt = 'You do not have permission for this command'
            print('Not moderator')
            await ctx.channel.send(fmt)
        # Tell the user they don't have the moderator role or pass
    else:
        fmt = 'You did not input correct save'
        print('wrong save form')
        await ctx.channel.send(fmt)
    # if ctx.message.attachments:
    #     print(5)
    #     await ctx.message.attachments[0].save("newtesting.png", seek_begin=True, use_cached=False)

    


    

bot.run(TOKEN)