import discord
import time
import asyncio

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()



@client.event
async def on_message(message):
    if message.content.find("!hello") != -1:
        await message.channel.send("Hi")

    if message.content.startswith("!roominfo"):
        roominfo = discord.Embed(title= 'test', description='test', colour=3447003)
        roominfo.add_field(name='', value='Popp Martin Student Union 252')

        await message.channel.send(embed=roominfo)



client.run(token)
