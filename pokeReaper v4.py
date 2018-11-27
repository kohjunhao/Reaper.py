

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

copy = True
catch = False

level = True

def poke_paste(string):
    pyperclip.copy(string)
    pyautogui.typewrite('\n')
    
    pyautogui.keyDown('ctrl')
    pyautogui.typewrite('v')
    pyautogui.keyUp('ctrl')
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
            return
        return
        
    if message.content.startswith('p!'):
        await client.delete_message(message)

    if message.content.startswith('vote:'):
        await client.add_reaction(message,'check')
        await message.add_reaction(message,'U+274E')
        return

            
    if 'exp' == message.content.lower() or 'spam' == message.content.lower():
        #if message.author.id == '234597388164005890':
        await client.delete_message(message)
        return


    try:
        embed = message.embeds[0]
    except Exception:
        name = message.author.name
        name = name.split('#')[0]
        msg = message.content
        msg = msg.replace('fuck','f**k').replace('bitch','b**ch')
        if len(msg)>80:    
            print(name+': '+msg[:100]+'.....')
        else:
            print(name+': '+msg)
    else:
        try:
            desc = embed['description']
        except KeyError:
            print(embed)
            
        print('Embed: '+desc)
        
        if 'level 100!' in desc and level:
            if 'Espeon' in desc:
                poke_select(54)
            if 'Vaporeon' in desc:
                poke_select(329)
            if 'Salamence' in desc:
                poke_select(237)
            if 'Porygon-Z' in desc:
                poke_select(163)
            if 'Blaziken' in desc:
                poke_select(31)
            if 'Celebi' in desc:
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
                return

            identity = text[int(index)+40:int(index)+50000]
            while True:
                try:
                    name = identity[:identity.index('_(Pok%C3%A9mon)')].lower()
                    if not name.isalpha():
                        raise ValueError
                    
                except ValueError:
                    try:
                        index = identity.index('https://bulbapedia.bulbagarden.net/wiki/')
                        identity = identity[int(index)+40]
                    except ValueError:
                        try:
                            index = text.index('https://pokemondb.net/pokedex/')
                        except ValueError:
                            msg = 'i am a stupid bot who can\'t find anything'.format(message)
                            await client.send_message(message.channel, msg)
                            return
                        else:
                            identity = text[int(index)+30:int(index)+25000]
                            name = identity[:identity.index('"')].lower()
                            if not name.isalpha():
                                msg = 'i am a stupid bot who can\'t find anything'.format(message)
                                await client.send_message(message.channel, msg)
                                return
                            if catch:
                                poke_catch(name)
                                return
                            if copy:
                                pyperclip.copy(name)
                                return
                            if not catch and not copy:
                                msg = name.format(message)
                                await client.send_message(message.channel, msg)
                                return
                        
                        
                            
                else:
                    if catch:
                        poke_catch(name)
                        return
                    if copy:
                            pyperclip.copy('p!catch '+name)
                            return
                    if not catch and not copy:
                        msg = name.format(message)
                        await client.send_message(message.channel, msg)
                        return
            
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

    if message.author.id == '234597388164005890':
        if 'p!' in message.content:
            await client.delete_message(message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
