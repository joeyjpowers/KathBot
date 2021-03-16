import discord
import os
import json
import random

client = discord.Client()

punJson = json.loads(open('jsons/puns.json').read())

def get_pun():
  return punJson[random.randrange(0, len(punJson))]["Pun"]

def get_kath():
  path = "./kathPics"
  random_pic = random.choice([
      x for x in os.listdir(path)
      if os.path.isfile(os.path.join(path, x))
  ])
  return (random_pic)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return

    if msg.startswith('!pun'):
        pun = get_pun()
        await message.channel.send(pun)

    if msg.startswith('!duck'):
        await message.channel.send(file=discord.File("ducks/duck" + str(random.randrange(1, 13)) + '.jpg'))

    if msg.startswith('!kath') or msg.startswith('!joey'):
        random_pic = get_kath()
        await message.channel.send(file=discord.File("kathPics/" + random_pic))

    if msg.startswith('!turkeyorham') or msg.startswith('!hamorturkey'):
        await message.channel.send(file=discord.File("pics/turkey.jpeg"))
    
    if msg.startswith('!sharpormild') or msg.startswith('!mildorsharp'):
        await message.channel.send(file=discord.File("pics/sharp.jpeg"))

    if msg.startswith('!buzzorwoody') or msg.startswith('!woodyorbuzz'):
        await message.channel.send(file=discord.File("pics/buzz.jpeg"))

    if msg.startswith('!happybirthday'):
        await message.channel.send("Happy 19th birthday Kath! I made this discord bot as a little gift for you, hope you like it. You can use !pun to get a random pun, !duck to get a random picture of a duck, and either !kath or !joey to get a random picture of us together. There are also some hidden commands, so try to find them!")
      
    if msg.startswith('!help'):
        await message.channel.send("Type !happybirthday to get more information on what this bot can do.")

client.run(os.getenv('TOKEN'))