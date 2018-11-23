

# POKEMON ON DISCORD

import sys
import pyperclip
import pyautogui
import time
import random
import discord
import urllib.request

sys.setrecursionlimit(99999999)


TOKEN = 'MjQ0NTI4ODk4MDE1MTAwOTI5.DthMaQ.gfC1QSIvcd48Eu-wGgB9ZFpqhUI'

client = discord.Client()

write = True
catch = False
level = True

def poke_paste(string):
    pyperclip.copy(string)
    pyautogui.typewrite('\n')
    pyautogui.keyDown('ctrl')
    pyautogui.typewrite('v')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite('\n')

    pyperclip.copy('exp')


def poke_catch(name):
    name = name.replace('_',' ')
    poke_paste('p!catch '+name)
    
def poke_select(number):
    number = str(number)
    poke_paste('p!select '+number)



def poke_search(url,write=False):
    req = urllib.request.Request(
        url,
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    r = urllib.request.urlopen(req)
    text = r.read().decode('utf-8')

    if write:
        file = open('search.txt','w')
        text2 = text.encode('utf-8')
        file.write(str(text2))
        file.close()

    return text
                
@client.event
async def on_message(message):
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!bot'):
        await client.delete_message(message)
        msg = message.content.split(' ')
        msg = ' '.join(msg[1:])
        print(message.author.id)
        if message.author.id == '234597388164005890':
            msg = (msg).format(message)
            await client.send_message(message.channel, msg)


    try:
        embed = message.embeds[0]
    except Exception:
        if len(message.content)>100:    
            print('Message: '+message.content[:100]+'.....')
        else:
            print('Message: '+message.content)
    else:
        try:
            desc = embed['description']
        except KeyError:
            print(embed)
            
        print('Embed: '+desc)
        
        if 'level 100!' in desc and level:
            if 'Shaymin' in desc:
            	poke_select(75)
            if 'Venusaur' in desc:
            	poke_select(3)
            if 'Meowstic' in desc:
            	poke_select(49)
            
        if desc.startswith('Guess the pokémon'):
            print(embed)
            url = embed['image']['url']
            google = 'https://images.google.com/searchbyimage?image_url='+url
            #msg = google.format(message)
            #await client.send_message(message.channel, msg)

            text = poke_search(google,write)

            try:
                index = text.index('https://bulbapedia.bulbagarden.net/wiki/')
            except ValueError:
                msg = 'i am a stupid bot who can\'t find anything'.format(message)
                await client.send_message(message.channel, msg)

            identity = text[int(index)+40:int(index)+100000]
            while True:
                try:
                    name = identity[:identity.index('_(Pok%C3%A9mon)')]
                    break
                except ValueError:
                    index = indentity.index('https://bulbapedia.bulbagarden.net/wiki/')
                    identity = identity[int(index)+40]
            msg = name.format(message)
            await client.send_message(message.channel, msg)
            if catch:
                poke_catch(name)
            
    if message.content.startswith('!pokemon') or message.content.startswith('p!search'):
        pokemon = message.content.split(' ')[1]
        url = 'https://www.google.com/search?q=pokedex+'+pokemon
        text = poke_search(url)
        try:
            index = text.index('https://pokemondb.net/pokedex/')
            link = text[int(index):int(index)+50].split('"')[0]
        except ValueError:
            link = 'No pokemon found named '+pokemon
        msg = (link).format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!search'):
        query = message.content.split(' ')[1]
        url = 'https://www.google.com/search?q='+query.replace(' ','+')
        text = poke_search(url,True)
        index = text.index('https://')
        link = text[int(index):int(index)+250].split('"')[0]
        print(link)
        msg = (link).format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.lower().startswith('test'):
        msg = 'I\'m tired. {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
