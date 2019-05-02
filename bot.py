import discord
import hiddenstuff
import random
import time
import asyncio
from discord.ext import commands
from hiddenstuff import token 

###   globals   #
bot = commands.Bot(command_prefix='~')
bot.description = 'ooga booga(lol ur a nigger if ur reading this:flan:) the symbol is ~. that is the key. the secret to a long and full life. heh, not that you\'d do anything with a long and full life. lol. u even got a gf? and ur what? 21? 23? 27!? jesus christ lmfao anyway heres how to use me or whatever'
topics = []
in_db  = []

db = open("database","a+")
db.close()

   
###   functions   ####   
def randomize():
    #old = topics[0]
    random.shuffle(topics)
    return topics[0]
    
def readdata():
    db = open("database","r")
    if db.mode == 'r':
        contents = db.read()
    temp = contents.split(',')
    for t in temp:
        in_db.append(t)
        topics.append(t)
    print('read data: ')
    for t in topics: 
        print('\t'+t)
    print()

    ###   commands   ###
#@bot.command()
async def watchclock(ctx):
    """ listen guys this is harder than it looks and doesnt work at all so dont even use it ok """
    while True:
        await asyncio.sleep(1)#might be much
        #print (time.clock())
        if int(time.clock()) % 5000 is 0:
            setindex( random.randint(0, len(topics)-1))
            print('new index', getindex())
            await asyncio.sleep(1)
            await ctx.send("OK FAGETS NEW TOPIC UHHH OK NOW WEIR GNA TALK ABOUT" + topics[getindex()])
            print('new topic: ', topics[getindex()])

@bot.command()
async def addtopic(ctx):
    """what do u think it does"""
    str = ctx.message.content[10:]
    str = str.strip()
    topics.append(str)
    print ('called addtopic with input:', str)
    await ctx.send('added')

@bot.command()
async def alltopics(ctx):
    """honestly its kinda self explanatory"""
    out = ''
    for s in topics:
        out += s + '\n'
    print ('called alltopics\n', out)
    if out:
        await ctx.send(out)
    else:
        print('empty')
        await ctx.send('their r no topics dumbarse lol get ur shit together')
                    
@bot.command()
async def topic(ctx):
    """tells u whatthe fucg everypony is talking about in dis chat"""
    print("viewtopic")
    await ctx.send(topics[0])

@bot.command()
async def newtopic(ctx):
    topic = randomize()
    print("newtopic", topic)
    await ctx.send("okay dude whatever you say. you can just let me go at my pace but NOOOOOOOO mister fucking freedy has to do it his way. whatever.\ntHE NEW TOPIC IS..." + topic + "...")
    
@bot.command()
async def savetopics(ctx):
    """ok maybe this is a bit less self explanatory so i'll give you and explanation. ok? alright? ok its actually pretty simple. this saves all your topics to a permanent pool of topics... forever... so i never lose them... forever...."""
    out = ''
    db = open('database','a+')
    for s in topics:
        if s not in in_db:
            out += ',' + s
    db.write(out)
    print(out, "saved to database file")
    await ctx.send("digital memory force pushed into savability matrix")
        
###   script   ###    
readdata()
print('connected')
bot.run(token)
print('disconnected')

# kkk 1488 heil hitler fuck the new world order
    