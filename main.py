
import os
import sys
import time
import random
import discord
import urllib.request

creatorID = os.environ.get("CREATOR_ID")

from keep_alive import keep_alive

# CREATES INSTANCE OF CLIENT VARIABLE
client = discord.Client()
                
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!!bot'):
        await client.delete_message(message)
        msg = message.content.split(' ')
        msg = ' '.join(msg[1:])
        if message.author.id == creatorID:
            msg = (msg).format(message)
            await client.send_message(message.channel, msg)
            return
        return

    try:
        embed = message.embeds[0]
    except Exception:
        # EXCEPTION RAISED MEANS MESSAGE IS PLAINTEXT
        name = message.author.name
        name = name.split('#')[0]
        msg = message.content
        print(name+': '+msg)
    else:
        # MESSAGE IS AN EMBED
        try:
            desc = embed['description']
            print('Embed: '+desc)
        except KeyError:
            pass#print(embed)
        
        
        
    if message.content.lower().startswith('yeetsketit'):
        msg = 'fuck off nigga, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        return


    if message.content.lower().startswith('!!math'):
        msg = message.content
        answer = str(eval(msg.split('math ')[1]))
        choice = random.randint(0,2)
        if choice == 1:
            msg = ('hahaha nigga simple, answer is '+answer).format(message)
        elif choice == 2:
        	msg = ('fuck off, answer so easy also need ask, legit waste my time').format(message)
        #this is a condition where choice =0
        else:
            msg = ('fucking idiot lmao so easy also don\'t know, '+answer).format(message)
        
        await client.send_message(message.channel,msg)

    if message.content.lower().startswith('!!choose'):
        msg = msg.split('choose')[1].split('|')
        length = len(msg)
        choice = random.randint(0,length-1)
        chosen = msg[choice]
        msg = ('simple decision also need me to do wtf. --- '+chosen.strip()).format(message)
        await client.send_message(message.channel,msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="with Python 3.6.7"))

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)

