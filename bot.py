import discord
from discord.ext import commands

import time
import asyncio




def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

bot = commands.Bot(command_prefix='!')



token = read_token()


event1 = discord.Embed(title=None)


@bot.event
async def on_ready():
    print(f'Bot is ready')


@bot.event
async def on_message(message):
    id = bot.get_guild(574323535368028162)
    channels = ["dm-bot"]



    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")
        print("Says hi")
    elif message.content.startswith('!roominfo'):
        embed = discord.Embed(title="Room Info",
                              description="This information to help those that need to reserve rooms",
                              color=discord.Color.blue())
        embed.add_field(name="Location to get table", value="Front desk of Union (BE EARLY!)", inline=False)
        embed.add_field(name="Location to reserve rooms for Events",
                        value="Popp Martin Student Union 252 \n 704-687-7872  \nMonday - Friday \n 8:00 A.M - 5:00 P.M ",
                        inline=False)
        await message.channel.send(embed=embed)
        print("send room info")

    if message.content.startswith('$w'):
        await message.channel.send("5 you are pretty good.... 4 you ight ")

    await bot.process_commands(message)

@bot.command(brief='Display event')
async def event(ctx):
    global event1
    await ctx.send(embed=event1)

@bot.command(brief='sets date of the event')
async def setDate(ctx,message):
    global event1
    event1.add_field(name="Date", value=message, inline=False)
@bot.command(brief='DOES NOT WORK')
async def rmDate(ctx):
    global event1
    event1.remove_field(4)
@bot.command(brief='add a location')
async def setLocation(ctx,*,message):
    global event1
    event1.add_field(name="Location", value=message, inline=False)
@bot.command(brief='DOES NOT WORK')
async def rmLocation(ctx):
    global event1
    event1.remove_field()
@bot.command(brief= 'adds a flyer')
async def setFlyer(ctx,*,message):
    global event1
    event1.set_image(url=message)

@bot.command(brief='Clears all fields')
async def clearFields(ctx):
    global event1
    event1.clear_fields()
@bot.command(brief='Creates a title for event')
async def setTitle(ctx,*,message):
    global event1
    event1 = discord.Embed(title= message)
@bot.command(brief='Deletes current event')
async def hardReset(ctx):
    global event1
    event1 = discord.Embed(title="Awww shit here we go again")
    await ctx.send("Somebody done fucked up")



bot.run(token)
