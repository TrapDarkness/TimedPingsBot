# bot.py
import os
import random
import discord
from discord import file

import asyncio
from datetime import datetime, timedelta
import time
import sched

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

@bot.event
async def on_message(message):
    if "69" in message.content and ("527866997396996096" not in message.content):
        if random.randint(1,2) == 1:
            await message.channel.send("*every time*")
        else:
            await message.channel.send("*Nice.*")
    if ("So you have chosen death" in message.content) and (str(message.author) == "!hellotheredoriyah#6535"):
        await message.channel.send("https://tenor.com/view/lotr-so-you-have-chosen-death-chosen-death-lord-of-the-rings-gif-15767548")
        print(message.author)
    if "Omae wa mou shindeiru" in message.content:
        await message.channel.send("*Nani?!*")
    if "420" in message.content:
        if random.randint(1,2) == 1:
            await message.channel.send("*whiff*")
        else:
            await message.channel.send("https://1d4chan.org/images/8/8a/Necro_blunt_hit.jpeg ")
            await message.channel.send("This is what happens when you smoke the necronomicon")
    if ("aayyyy" in message.content) and (str(message.author) == "Card#4050"):
        print(message.author)
        path_file = os.path.join("C:/Users/novalabsrobotics/Bot/Games and Stuff/Yang", "yang_eyyy.png")  
        print(path_file)
        await message.channel.send(file=discord.File(path_file))
        
    await bot.process_commands(message)

@bot.command(name='roll_dice', help='Simulates rolling dice. Input in form "roll_dice X Y" X is number of dice to be rolled, and Y is the number of sides on those dice. Max is 69')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    if number_of_dice > 69:
        number_of_dice = 69
    if number_of_sides > 31415:
        number_of_sides = 31415
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

deleted_message = "Delete?"
test_array = []
@bot.event
async def on_message_delete(message):
        fmt = '{0.author} has deleted the message: {0.content} at {0.created_at}'
        # in {0.guild}R
        global test_message
        test_message = message
        # print(test_message)
        global test_array
        if len(test_array) == 6:
            test_array.pop(0)

        test_array.insert(0, message)
        
        print(test_array)
        author = str(message.author)
        content = str(message.content)
        date_time = str(message.created_at)
        channel = str(message.channel)
        fmt = author + ' has deleted the message: ' + content + " at " + date_time + " in " + channel
        open_file = open("DeletedMessages.txt", "a")
        # open_file.write(fmt.format(message))
        open_file.write(fmt)
        open_file.write("\n")
        open_file.close()

        # await message.channel.send(fmt.format(message))




@bot.command(name='snipe', help='See deleted messages. Input command in "}snipe X" form, it will return the past X messages, up to 5')
async def snipe(ctx, depth :int):
    # fmt = '{0.author} has deleted the messages: {0.content}'
    # message_array = []
    for item in test_array[0:depth]:
        fmt = '{0.author} has deleted the message: {0.content}'
        if "!hellotheredoriyah#6535" in fmt.format(item) and fmt.format(item).count(".") == 2:
            await ctx.channel.send("*Nice Try*")
        else:
            await ctx.channel.send(fmt.format(item))

    # print(test_message)
    # await ctx.send(deleted_message)
    # print(test_array)
    # await ctx.channel.send(fmt.format(test_message))

@bot.command(name='simp', help='Save to database and access from it. format command as "}simp charactername filename save" where save can be either save or pull, depending on if one wants to save the image or pull it from the database. In addition, for moderators, can use "delete" in place of save to remove offending files. Filename is the desired name of the file when saved, not what the file is currently called on your device. Charactername is the name of the character or ship. make sure the file is attached to the same message as the command not sent in separate ones')
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
                fmt = 'File Succesfully Saved!'
                print("File Succesfully Saved!")
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

@bot.command(name='saoa', help='Responds with a random quote from Sword Art Online Abridged')
async def random_saoa(ctx):
    saoa_quotes = [
        "Of course not. Obviously, it was a hit by the mermaid mafia paid in leprechaun gold. But who was the puppet master? The unicorns? No, they’ve had a feud with going with the mermaids for years.",
        'Kuradeel: "Enough! How dare you mock me in such a manner!" \n Kirito: "Well, how would you like me to mock you, then? I take requests."',
        'Yoko: Schmitt used to review games back in the real world. But ever since hes been trapped in here, hes been terrified that his more... verbose commenters are going to make good on their threats. \n Schmitt: I used to laugh at their comments! You hear me? LAUGH! But now, what if they actually DO chop off my limbs, rip out my intestines, and ride me like some sort of meat toboggan?! \n Kirito: Ya hear that, Asuna? "Meat Toboggan." Try gettin THAT image out of your head. Gripping his entrails like the reins of Santas sleigh, streaking through the fresh morning snow on a trail of bile and gore, as his eyes beg the same question as the horrified children in his wake: "Why...?"', 
        "Boss won't get off your back? Girlfriend won't stop nagging you? Did that fuckstick Tiffany sell you a bullshit dagger that broke almost immediately despite the fact that you spent half your goddamn Col on it? Have you considered... murder?",
        "Awww. You think they're a threat. Show's about to start. Careful though, The first three rows are a splaaaash zooone *Maniacal Laughter*",
        'https://tenor.com/view/sao-sword-art-online-abridged-you-are-an-adequate-meatshield-no-one-can-ever-take-that-away-from-you-gif-16345365'

    ]

    response = random.choice(saoa_quotes)
    await ctx.send(response)   

@bot.command(name = 'simp_list', help='format as "simp_list", which lists all character folders, or "simp_list character", which lists all filenames in a single character folder')
async def simp_list(ctx, character = "None"):
    print("simp_list")
    guild = ctx.message.guild.name
    directory = character
        
    # Parent Directories  
    parent_dir = "c:/Users/novalabsrobotics/Bot/"
    parent_dir += guild

    if character == "None":
        print('simp_list folders')
        path_dir = os.listdir(parent_dir)
        print(path_dir)
        await ctx.channel.send(path_dir)
    else:
        print('simp_list character')
        path_file = os.path.join(parent_dir, directory)
        path_dir_char = os.listdir(path_file)
        print(path_dir_char)
        await ctx.channel.send(path_dir_char)


@bot.command(name='game_list', help='Format as "game_list find_game GAME" which finds all users who play GAME. "game_list add_game GAME " which will add GAME to your list of played games, "game_list remove_game GAME" removes GAME from your list of played games, or "game_list list USER" lists all games USER plays')
async def game_list(ctx, command, game = "None"):

    game = game.lower()
    author_name = str(ctx.message.author)
    guild = ctx.message.guild.name
        
    # Parent Directories  
    parent_dir = "c:/Users/novalabsrobotics/Bot/Played_Games_Lists/"
    parent_dir += guild
    within_parent_dir = parent_dir + "/"
    try:  
            os.mkdir(parent_dir) 
            print("Directory '% s' created for server" % guild)  
    except OSError as error:  
        print(error)  

    if command == "add_game":
        open_file = open(within_parent_dir + author_name + "played_games.txt", "a")
    # open_file.write(fmt.format(message))
        open_file.write(game)
        open_file.write("\n")
        open_file.close()
        # user_game_dictionary[author_name] = game
        # user_game_dictionary[author_name] += ' Test'
        await ctx.channel.send(game + " successfully added to list")
        # print(user_game_dictionary[author_name])
    elif command == "remove_game":
        with open(within_parent_dir + author_name + "played_games.txt", "r") as f:
            lines = f.readlines()
        with open(within_parent_dir + author_name + "played_games.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != game:
                    f.write(line)  
        await ctx.channel.send(game + " successfully removed from list")

    elif command == "find_game":
        path_dir = os.listdir(parent_dir)
        print(path_dir)
        users_that_play_game = []
        for file in path_dir:
            print(5)
            print(file)
            with open(within_parent_dir + file, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip("\n") == game:
                        users_that_play_game.append(file.removesuffix("played_games.txt")) 
        await ctx.channel.send(users_that_play_game)

    elif command == "list":
        with open(within_parent_dir + str(game) + "played_games.txt", "r") as f:
            lines = f.readlines()
        lines_stripped = []
        for line in lines:
            stripped = line.replace("\n", "")
            lines_stripped.append(stripped)
        print(lines_stripped)
        await ctx.channel.send(lines_stripped)
        # else:
        #     await ctx.channel.send('User has no games listed')

# @bot.command(name='reminder', help='Set a reminder')
# async def reminder(ctx, alarm_time):
#     await bot.wait_until_ready()
#     while not bot.is_closed:
#         channel = ctx..channel
#         messages = ('Test')
#         f = '%H:%M'

#         now = datetime.strftime(datetime.now(), f)
#         # get the difference between the alarm time and now
#         diff = (datetime.strptime(alarm_time, f) - datetime.strptime(now, f)).total_seconds()

#         # create a scheduler
#         s = sched.scheduler(time.perf_counter, time.sleep)
#         # arguments being passed to the function being called in s.enter
#         args = (bot.send_message(channel, ctx), )
#         # enter the command and arguments into the scheduler
#         s.enter(seconds, 1, bot.loop.create_task, args)
#         s.run() # run the scheduler, will block the event loop
# @bot.command(name='howsus', help='random number from 0-100 for sus%')
# async def howsus(ctx, id = None):
#     sus_percent = random.randint(0, 100)
#     response = ">>> **sus significance determination autonomous operation** \n \n"
#     print("hi")
#     if id == None:
#         response += "You are " + str(sus_percent) + "% *sus*"
#         print("no id")
#     else:
#        response += id + " is " + str(sus_percent) + "% *sus*"
#        print(id)
#     await ctx.channel.send(response)
#     # await ctx.channel.send("cat")

# @bot.command(name='howgay', help='random number from 0-100 for gay%')
# async def howgay(ctx, id = None):
#     gay_percent = random.randint(0, 100)
#     response = ">>> **gay proportion determination autonomous operation** \n \n"
#     print("hi")
#     if id == None:
#         response += "You are " + str(gay_percent) + "% *gay*"
#         print("no id")
#     else:
#        response += id + " is " + str(gay_percent) + "% *gay*"
#        print(id)
#     await ctx.channel.send(response)

@bot.command(name='how', help='Format "}how X" random number from 0-100 for "X"%')
async def howgay(ctx, word, id = None):
    word_percent = random.randint(0, 100)
    response = ">>> **" + word + " proportion determination autonomous operation** \n \n"
    print("hi")
    if id == None:
        response += "You are " + str(word_percent) + "% *" + word + "*"
        print("no id")
    else:
       response += id + " is " + str(word_percent) + "% *" + word + "*"
       print(id)
    await ctx.channel.send(response)
    
@bot.command(name='keypad', help='Input Notation for BBTAG')
async def keypad(ctx):
    guild = ctx.message.guild.name
    #directory = "Miscellaneous"
        
    # Parent Directories  
    parent_dir = "c:/Users/novalabsrobotics/Bot/Miscellaneous"
    #parent_dir += guild

    # Path  
    path = os.path.join(parent_dir, guild)  
        
    # Create the directory  
    # 'charactername'  
    try:  
        os.mkdir(parent_dir) 
        print("Directory '% s' created for server" % guild)  
    except OSError as error:  
        print(error)   

    try:  
        os.mkdir(path) 
        print("Directory '% s' created for character" % guild)  
    except OSError as error:  
        print(error)   

    filename = "keypad_notation"            
    filename += ".png"
    print(filename)
    flags = os.O_RDWR | os.O_CREAT 

    # path = os.path.join(path, filename)
    # await ctx.channel.send(os.listdir(path))
    path_file = os.path.join(parent_dir, guild, filename)  
    print(path_file)
    # await ctx.channel.send(os.open(path1, flags))

    await ctx.channel.send(file=discord.File(path_file))

    # await ctx.channel.send(file=discord.File(filename))

    # with open(parent_dir, 'rb') as fp:
        #     await ctx.channel.send(file=discord.File(fp, filename))

# @bot.command(name='pin', help='"Pins" messages')
# async def pin(ctx, pin_name, pin):

#     pin = pin.lower()
#     author_name = str(ctx.message.author)
#     guild = ctx.message.guild.name
        
#     # Parent Directories  
#     parent_dir = "c:/Users/novalabsrobotics/Bot/Pinned_Messages/"
#     parent_dir += guild
#     within_parent_dir = parent_dir + "/"
#     try:  
#             os.mkdir(parent_dir) 
#             print("Directory '% s' created for server" % guild)  
#     except OSError as error:  
#         print(error) 

#     path_dir = os.listdir(within_parent_dir)
#     print(path_dir)
#     if (pin_name +".txt") not in path_dir:

#         open_file = open(within_parent_dir + pin_name + ".txt", "w")
#     # open_file.write(fmt.format(message))
#         open_file.write(pin)
#         open_file.write("\n")
#         open_file.close()
#         # user_game_dictionary[author_name] = game
#         # user_game_dictionary[author_name] += ' Test'
#         await ctx.channel.send(pin_name + " successfully added to list")
#         # print(user_game_dictionary[author_name])

#     elif pin_name == "list" and pin == "":
#         print(path_dir)
#         await ctx.channel.send(path_dir)

#     else:
#         f = open(within_parent_dir + pin_name + ".txt", "w")
#         lines = f.readlines()
#         lines_stripped = []
#         for line in lines:
#             stripped = line.replace("\n", "")
#             lines_stripped.append(stripped)
#         print(lines_stripped)
#         await ctx.channel.send(lines_stripped)

bot.run(TOKEN)
