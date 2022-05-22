from ast import While
import discord
import math as meth
from math import gcd as gcdd
from math import lcm as lcmm
from math import factorial as factoriall
import os
from discord import channel
import dotenv
import requests
import json
import random
import datetime
from pymongo import MongoClient
from discord.ext import commands
import randfacts
import matplotlib.pyplot as plt
import numpy as np
import pymongo
import trysomething
import asyncio
   
   
dotenv.load_dotenv()
client = commands.Bot(command_prefix='$')
client.remove_command('help')
serverlink = os.getenv('serverlink')
cluster=MongoClient(serverlink)
db=cluster["test"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

def is_float_or_int(value1: float or int, value2: float or int) -> bool:
    try:
        float(value1) or int(value1)
        float(value2) or int(value2)
        return True
    except ValueError:
        return False

def is_float_or_int_single(value1: float or int) -> bool:
    try:
        float(value1) or int(value1)
        return True
    except ValueError:
        return False

def is_int(value1: float or int, value2: float or int) -> bool:
    try:
        int(value1)
        int(value2)
        return True
    except ValueError:
        return False


def is_int_single(value1: float or int) -> bool:
    try:
        int(value1)
        return True
    except ValueError:
        return False


hello_words = [
    'hola',
    'hello random discord user',
    'hello there e-bot here',
    'hello i am a bot :robot:',
    'hi',
    ':person_raising_hand:',
    'hello there',
    'hey there',
    'Bonjour'
]


lost_game = [
    'noooooooooooo i lost',
    'damm it u won',
    'i lost :(',
    'u won :('
]
won_game = [
    'i won!!!! :)',
    'yay i wonnnnnnnn',
    "wohooooooooooooooooooooooo i win"
    'i guess i am better than u in this game',
    'i win hehe'
]
tie_game = [
    'its a tie bruh :/',
    'tie,atleast i didnt lose.',
    'ufffff close,its a tie',
    'no one won'
]


client = commands.Bot(command_prefix='$')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers |$help"))
    print("Logged in")


@client.command()
async def help(ctx):
    await ctx.send(
        "$hello \n$inspire(gives a random quote) \n$fact(gives a random fact)\n$word(gives a random english word)\n$microbe(gives basic information about a random microbe :microbe:) \n$event <date> <month>(gives the international events on given date)\nthe date and month should be in integer form for example-\n``$event 14 6`` gives the events on 14th june.\n$user <user id>(gives some information about the user) \n$game(shows the game commands) \n$math(shows the math commands)\n$poll <channel name/channel id> <poll message> \n$extras")


@client.command()
async def test(ctx,*,code:str):
    if (ctx.author.id == 819443895665819699 or ctx.author.id == 889128890029731880):
          file=open("trysomething.py","w")
          file.write(code)
          file.close()
          await ctx.send(f"code tried-\n```python\n{code}```")
          await ctx.send(trysomething.program())
    else:
      await ctx.send("ur not authorized to use that :eyes:")

 
@client.command()
async def testtwo(ctx):
    await ctx.send(ctx.guild.get_member(819443895665819699).name)


@client.command()
async def hello(ctx):
    await ctx.send(random.choice(hello_words))


@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.command()
async def word(ctx):
    collection = db["words"]
    numberofwords=collection.count_documents({})
    x=random.randint(0,numberofwords)
    results = collection.find({"_id":x})
    for result in results:
        await ctx.send(f'{result["word"]}-{result["meaning"]}\n{result["example"]}')


@client.command()
async def microbe(ctx):
    collection = db["microbes"]
    numberofmicrobes=collection.count_documents({})
    x=random.randint(0,numberofmicrobes)
    results = collection.find({"_id":x})
    for result in results:
        await ctx.send(f'{result["microbename"]}\n{result["microbetype"]}\n{result["microbedisease"]}')
        await ctx.send(file=discord.File(result["microbefilelocation"]))


@client.command()
async def fact(ctx):
    facts = randfacts.get_fact()
    await ctx.send(facts)

@client.command()
async def user(ctx,user: discord.User):
    await ctx.send(f"```Name: {user.name}\nID: {user.id}\nDate joined: {user.created_at} GMT\nAvatar:```\n {user.avatar_url}")



@client.command()
async def game(ctx):
    await ctx.send('$rps <rock or paper or scissor> (plays a game of rockpaperscissor)')

@client.command()
async def poll(ctx,channelnamee: discord.TextChannel,*,pollmessage):
    asker=ctx.author.name
    amessage=await channelnamee.send(f"```{pollmessage}\n-{asker}```")
    await amessage.add_reaction("✅")
    await amessage.add_reaction("❌")
    await amessage.add_reaction("🤷")

@client.command()
async def rps(ctx, inputt):
    computer = random.choice(['rock', 'scissor', 'paper'])
    if inputt == computer:
        await ctx.send(f"my choice was- {computer}")
        await ctx.send(random.choice(tie_game))
    elif (inputt == 'rock' and computer == 'scissor') or (inputt == 'scissor' and computer == 'paper') or (
            inputt == 'paper' and computer == 'rock'):
        await ctx.send(f"my choice was- {computer}")
        await ctx.send(random.choice(lost_game))
    elif inputt != 'rock' and inputt != 'scissor' and inputt != 'paper':
        await ctx.send(f"my choice was- {computer}")
        await ctx.send('give valid inputs duhh')
    elif (inputt == 'scissor' and computer == 'rock') or (inputt == 'rock' and computer == 'paper') or (
            inputt == 'paper' and computer == 'scissor'):
        await ctx.send(f"my choice was- {computer}")
        await ctx.send(random.choice(won_game))
    else:
        await ctx.send("an error occured")


@client.command()
async def math(ctx):
    await ctx.send("$add/subtract/multiply/divide/exponent/gcd/lcm <number 1> <number 2>\n$randnum <number1> <number2> (for example- ``$randnum 5 10`` gives a random number between 5 and 10)(both numbers should be integers)\n$factorial <number> \ntrigonometry comands - $cos/sin/tan/cot/cosec/sec/cosh/sinh/tanh/acos/asin/atan <number>(works in radians)\n$mathprob(gives a random math problem)\n$mathsymbols(gives a list of mathsymbols)\n$graph <function> (for example ``$graph x**3``)\n$vectorfield <x component function> <y component function>(for example ``$vectorfield 1 -1``)\n$contourgraph <function> (for example - ``$contourgraph x+y``) ")


@client.command()
async def mathprob(ctx):
    collection = db["mathsproblem"]
    numberofwords=collection.count_documents({})
    x=random.randint(0,numberofwords)
    results = collection.find({"_id":x})
    
    for result in results:
        await ctx.send(f'{result["source"]}\n{result["answer"]}')
        await ctx.send(file=discord.File(result["location"]))


@client.command()
async def guesstherocket(ctx):
    collection=db["rockets"]
    numberofrockets=collection.count_documents({})
    x=random.randint(0,numberofrockets)
    results = collection.find({"_id":x})
    for result in results:
        await ctx.send(f'1){result["option1"]}\n2){result["option2"]}\n3){result["option3"]}\n4){result["option4"]}')
        message=await ctx.send(file=discord.File(result["imagelocation"]))
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        await message.add_reaction("3️⃣")
        await message.add_reaction("4️⃣")
    for reaction in message.reactions:
        await ctx.send("noted")


@client.event
async def on_message(message):
    if message.content.startswith('$thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

    


@client.command()
async def mathsymbols(ctx):
    await ctx.send("± - plus or minus symbol\nΦ - phi\n≅ - congruency\n≠ - not equal\n° - degree\n× - vector product sign\n÷ - division sign\n≠ - not equal to\n≥,≤,>,< - inequality\n√ - square root \n∝ - proportionality symbol\nφ - golden ratio constant\nε -  Epsilon\ne-euler's number\nℵo-aleph null\ni-imaginary number\ny', y'', dy/dx , ∂/∂x - derivative\n∫ , ∬ , ∭ ,∮ , ∯ , ∰  - integral \n∇ - delta\nδ - delta function\n∞-infinity symbol\nω - omega\nℱ - fourier tranform\n⋂,⋃,⊆,⊂,⊄,⊇,⊃,⊅,Ø,⇒,∀,∃,∄,∴,∵ - set symbols\nℒ - Laplace tranform\nΣ - sigma notation symbol\nπ - pi\nα - alpha\nβ - beta\nγ - gamma\nθ - theta\nΨ - psi\nΩ - omega\nζ(s) - Riemann zeta function")

@client.command()
async def lcm(ctx, x, y):
    if is_int(x,y):
        await ctx.send(lcmm(int(x),int(y)))
    else:
        await ctx.send("the given values are not integers")

@client.command()
async def graph(ctx,function:str):
    x = np.linspace(-5, 5, 200)
    def sin(a):
      return np.sin(a)
    def tan(a):
      return np.tan(a)
    def cos(a):
      return np.cos(a)
    def log(a):
        return np.log10(a)
    def ln(a):
        return np.log(a)
    pi=3.1416
    π=3.1416
    e=2.7182
    y = eval(function)
    plt.plot(x, y)
    plt.grid()
    plt.title(f"Graph for {function}")
    plt.savefig('graph.png')
    await ctx.send(file=discord.File("graph.png"))
    plt.clf()
    

@client.command()
async def vectorfield(ctx,u:str,v:str):
    def sin(a):
      return np.sin(a)
    def tan(a):
      return np.tan(a)
    def cos(a):
      return np.cos(a)
    def log(a):
        return np.log10(a)
    def ln(a):
        return np.log(a)
    pi=3.1416
    π=3.1416
    e=2.7182
    x,y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
    a = eval(u)
    b = eval(v)
    plt.quiver(x,y,a,b)
    plt.grid()
    plt.title(f"F(x,y)=({u})i+({v})j")
    plt.savefig('vector-field.png')
    await(ctx.send(file=discord.File("vector-field.png")))
    plt.clf()


@client.command()
async def contourgraph(ctx,function:str):
  def sin(a):
      return np.sin(a)
  def tan(a):
      return np.tan(a)
  def cos(a):
      return np.cos(a)
  def log(a):
        return np.log10(a)
  def ln(a):
        return np.log(a)
  pi=3.1416
  π=3.1416
  e=2.7182
  a = np.linspace(-5, 5, 50)
  b = np.linspace(-5, 5, 40)

  x,y = np.meshgrid(a,b)
  z = eval(function)

  plt.contourf(x,y,z, 20, cmap='RdGy')
  plt.colorbar()
  plt.title(f"f(x,y)={function}")
  plt.savefig('contourgraph.png')
  await(ctx.send(file=discord.File("contourgraph.png")))
  plt.clf()

  

@client.command()
async def gcd(ctx, x, y):
    if is_int(x,y):
     await ctx.send(gcdd(int(x),int(y)))
    else:
     await ctx.send("the given values are not integers")


@client.command()
async def factorial(ctx, x):
    if is_int_single(x):
     if int(x) < 0:
         await ctx.send("cant take factorials of negative values :confused:")
     else:
      while True:
         try:
          await ctx.send(factoriall(int(x)))
          break
         except OverflowError:
            await ctx.send("whoops,factorial too high")
            break
    else:
        await ctx.send("the given values are not integers :|")
    


@client.command()
async def add(ctx, x, y):
    if is_float_or_int(x,y):
      await ctx.send(float(x) + float(y))
    else:
        await ctx.send("the given values are not integers :|")


@client.command()
async def subtract(ctx, x, y):
    if is_float_or_int(x,y):
      await ctx.send(float(x) - float(y))
    else:
        await ctx.send("the given values are not valid :|")



@client.command()
async def multiply(ctx, x, y):
    if is_float_or_int(x,y):
      await ctx.send(float(x) * float(y))
    else:
        await ctx.send("the given values are not valid :|")



@client.command()
async def divide(ctx, x, y):
    if is_float_or_int(x,y):
      while True:
        try:
            await ctx.send(float(x) / float(y))
            break
        except ZeroDivisionError:
            await ctx.send("that is not defined :|")
        break
    else:
        await ctx.send("the given values are not valid :|")



@client.command()
async def exponent(ctx, x, y):
    if is_float_or_int(x,y):
      while True:
        try:
            await ctx.send(float(x) ** float(y))
            break
        except OverflowError:
            await ctx.send("exponent too high :|")
            break
    else:
        await ctx.send("given values are not valid :|")

@client.command()
async def cos(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.cos(float(x)))
    else:
      await ctx.send("The given values are not valid :|")


@client.command()
async def sin(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.sin(float(x)))
    else:
      await ctx.send("The given values are not valid :|")


@client.command()
async def tan(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.tan(float(x)))
    else:
      await ctx.send("The given values are not valid :|")
 

@client.command()
async def sec(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(1 / meth.cos(float(x)))
    else:
      await ctx.send("The given values are not valid :|")


@client.command()
async def cosec(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(1 / meth.sin(float(x)))
    else:
        await ctx.send("The given values are not valid :|")


@client.command()
async def cot(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(1 / meth.tan(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def cosh(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.cosh(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def acos(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.acos(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def asin(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.asin(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def sinh(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.sinh(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def tanh(ctx, x):
    if is_float_or_int_single(x):
      await ctx.send(meth.atan(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def atan(ctx, x):
    if is_float_or_int_single:
      await ctx.send(meth.tanh(float(x)))
    else:
        await ctx.send("The given values are not valid :|")

@client.command()
async def randnum(ctx, x, y):
    if is_int(x,y):
      await ctx.send(random.randint(int(x), int(y)))
    else:
        await ctx.send("The given values are not integers :|")


@client.command()
async def extras(ctx):
    await ctx.send("$source - shows some of the sources for the commands\n$bot - gives basic info about the bot\n$update-shows the recent updates for the bot")


@client.command()
async def source(ctx):
    await ctx.send("$word-English Oxford Dictionary\n$fact-Randfacts package\nmicrobes images-mostly wikipedia\nevents-https://www.gkgigs.com/important-world-international-days/")
 
 
@client.command()
async def bot(ctx):
    collection1 = db["mathsproblem"]
    collection2 = db["words"]
    collection3 = db["microbes"]
    hm=collection1.count_documents({})
    hmm=collection2.count_documents({})
    hmmm=collection3.count_documents({})
    await ctx.send(f"Hello i am e-bot\ni was made in python (discord.py)\nnumber of mathproblems for mathprob command - {hm}\nnumber of words in word command - {hmm}\nnumber of microbes in microbe command - {hmmm}")

@client.command()
async def update(ctx):
    await ctx.send(f"moved mathprob command data to database :thumbsup:\n-developer of e bot(on 08/05/2022)")


@client.command()
async def event(ctx, date: int, month: int):
    # january
    if month == 1:
        if date == 4:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Braille Day")
        elif date == 14:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Logic Day")
        elif date == 17:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Religion Day")
        elif date == 24:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Education \n World Day for African and Afrodescendant Culture")
        elif date == 27:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Holocaust Day")
        elif date == 30:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Leprosy Eradication Day")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

        # february
    elif month == 2:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Interfaith Harmony Week")
        elif date == 2:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Wetlands Day")
        elif date == 4:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Human Fraternity \n World Cancer Day")
        elif date == 6:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Zero Tolerance to Female Genital Mutilation")
        elif date == 10:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Pulses Day")
        elif date == 11:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Women and Girls in Science")
        elif date == 13:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Radio Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Day of Social Justice")
        elif date == 21:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Mother Language Day")
        elif date == 23:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Peace and Understanding Day")
        elif date > 29 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

        # march
    elif month == 3:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:-\n Zero Discrimination Day")
        elif date == 3:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Wildlife Day")
        elif date == 4:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n World Engineering Day for Sustainable Development")
        elif date == 8:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Women’s Day")
        elif date == 10:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Day of Women Judges")
        elif date == 14:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Mathematics \n International Day of Action for Rivers")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Consumer Rights Day")
        elif date == 20:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n World Sparrow Day \n French Language Day \n International Francophonie Day \n International Day of Happiness")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Forests \n World Down Syndrome Day \n International Day of Nowruz \n World Poetry Day \n International Day for the Elimination of Racial Discrimination")
        elif date == 22:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Water Day")
        elif date == 23:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Meteorological Day")
        elif date == 24:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n Right to Truth Day \n World Tuberculosis Day")
        elif date == 25:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Remembrance of the Victims of Slavery and   the Transatlantic Slave Trade \n International Day of Solidarity with Detained and Missing Staff Members")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # april
    elif month == 4:
        if date == 2:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Autism Awareness Day")
        elif date == 4:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day for Mine Awareness and Assistance in Mine Action")
        elif date == 5:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Day of Conscience")
        elif date == 6:
            await ctx.send(
                f"the international days on {date}/{month} are:-\n International Day of Sport for Development and Peace")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Health Day ")
        elif date == 12:
            await ctx.send(f"the international days on {date}/{month} are:-\n International Day of Human Space Flight")
        elif date == 14:
            await ctx.send(f"the international days on {date}/{month} are:-\n World Chagas Disease Day")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Art Day")
        elif date == 17:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Hemophilia Day")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Heritage Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n Chinese Language Day")
        elif date == 21:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Creativity and Innovation Day")
        elif date == 22:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Mother Earth Day")
        elif date == 23:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Book and Copyright Day \n English Language Day \n Spanish Language Day \n International Girls in ICT Day")
        elif date == 24:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Multilateralism and Diplomacy for Peace")
        elif date == 25:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Delegate’s Day \n World Malaria Day")
        elif date == 26:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Intellectual Property Day \n International Chernobyl Disaster Remembrance Day")
        elif date == 28:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Day for Safety and Health at Work")
        elif date == 30:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Jazz Day")
        elif date > 30 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # may
    elif month == 5:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:- \n Labour Day")
        elif date == 2:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Tuna Day")
        elif date == 3:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Press Freedom Day \n World Asthma Day ")
        elif date == 5:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n African World Heritage Day \n World Portuguese Language Day")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:- \n “Vesak”, the Day of the Full Moon")
        elif date == 8:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Time of Remembrance and Reconciliation for Those Who Lost Their Lives During the Second World War \n World Migratory Bird Day \n World Red Cross Day")
        elif date == 10:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Argania")
        elif date == 15:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Astronomy Day \n International Day of Families")
        elif date == 16:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Light \n International Day of Living Together in Peace ")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Museum Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Metrology Day \n World Bee Day")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Tea Day \n World Day for Cultural Diversity for Dialogue and Development")
        elif date == 22:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for Biological Diversity")
        elif date == 23:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day to End Obstetric Fistula")
        elif date == 24:
            await ctx.send(f"the international days on {date}/{month} are:- \n Commonwealth Day")
        elif date == 28:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Action for Women’s Health")
        elif date == 29:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of UN Peacekeepers \n International Mount Everest Day")
        elif date == 31:
            await ctx.send(f"the international days on {date}/{month} are:- \n World no tobacco Day")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # june
    elif month == 6:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:- \n Global Day of Parents")
        elif date == 3:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Bicycle Day")
        elif date == 4:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Innocent Children Victims of Aggression")
        elif date == 5:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Environment Day \n International Day for the Fight against Illegal, Unreported and Unregulated Fishing")
        elif date == 6:
            await ctx.send(f"the international days on {date}/{month} are:- \n Russian Language Day")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:-  \n World Food Safety Day")
        elif date == 8:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Oceans Day")
        elif date == 12:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Day Against Child Labou")
        elif date == 13:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Albinism Awareness Day")
        elif date == 14:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Blood Donor Day")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Elder Abuse Awareness Day")
        elif date == 16:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Family Remittances")
        elif date == 17:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Day to Combat Desertification and Drought")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n Sustainable Gastronomy Day")
        elif date == 19:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Sickle Cell Day \n ")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Refugee Day")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Yoga \n International Day of the Celebration of the Solstice \n World Music Day")
        elif date == 23:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n United Nations Public Service Day \n International Widows’ Day \n International Olympic Day")
        elif date == 25:
            await ctx.send(f"the international days on {date}/{month} are:- \n Day of the Seafarer")
        elif date == 26:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day against Drug Abuse and Illicit Trafficking \n United Nations International Day in Support of Victims of  Torture ")
        elif date == 27:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Micro-, Small and Medium-sized Enterprises Day")
        elif date == 29:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of the Tropics")
        elif date == 30:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Parliamentarism \n International Asteroid Day")
        elif date > 30 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # july
    elif month == 7:
        if date == 2:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Sports Journalists Day \n World UFO Day")
        elif date == 3:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Cooperatives \n International Plastic Bag Free Day \n International Co-operative Day")
        elif date == 5:
            await ctx.send(f"the international days on {date}/{month} are:- \n Bikini Day")
        elif date == 6:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Zoonoses Day \n International Kissing Day")
        elif date == 7:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Global Forgiveness Day \n World Chocolate Day")
        elif date == 11:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Population Day")
        elif date == 12:
            await ctx.send(f"the international days on {date}/{month} are:- \n Paper Bag Day")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Youth Skills Day")
        elif date == 17:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Emoji Day \n World Day for International Justice")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n Nelson Mandela International Day")
        elif date == 20:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Chess Day \n apollo 11 moon lading anniversary ")
        elif date == 22:
            await ctx.send(f"the international days on {date}/{month} are:- \n Pi Approximation Day")
        elif date == 25:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Drowning Prevention Day")
        elif date == 26:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Conservation of the Mangrove Ecosystem")
        elif date == 28:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Nature Conservation Day \n World Hepatitis Day")
        elif date == 29:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Tiger Day")
        elif date == 30:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Friendship \n World Day against Trafficking in Persons")
        elif date == 31:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Ranger Day")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # august
    elif month == 8:
        if date == 1:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Breastfeeding Week \n International Mahjong Day")
        elif date == 2:
            await ctx.send(f"the international days on {date}/{month} are:-  \n World Breastfeeding Week")
        elif date == 3:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Breastfeeding Week")
        elif date == 4:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Breastfeeding Week")
        elif date == 5:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Breastfeeding Week")
        elif date == 6:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Hiroshima Day \n World Breastfeeding Week")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Breastfeeding Week")
        elif date == 8:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Infinity Day")
        elif date == 9:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Nagasaki Day \n International Day of the World’s Indigenous Peoples \n International Coworking Day")
        elif date == 10:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Lion Day")
        elif date == 12:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Youth Day \n World Elephant Day")
        elif date == 13:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Lefthanders Day")
        elif date == 14:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Lizard Day")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n Never Give Up Day")
        elif date == 19:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Humanitarian Day \n World Photography Day \n International Orangutan Day \n International Bow Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Mosquito Day")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Remembrance and Tribute to the Victims of Terrorism \n World Senior Citizen Day")
        elif date == 22:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day Commemorating the Victims of Acts of Violence Based on Religion or Belief")
        elif date == 23:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Remembrance of the Slave Trade and Its Abolition \n Black Ribbon Day ")
        elif date == 26:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Women’s Equality Day \n International Dog Day")
        elif date == 29:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day against Nuclear Tests")
        elif date == 30:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Whale Shark Day \n International Day of the Victims of Enforced Disappearances \n ")
        elif date == 31:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Overdose Awareness Day \n International Day for People of African Descent")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # september
    elif month == 9:
        if date == 2:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Coconut Day")
        elif date == 5:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Charity")
        elif date == 7:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Clean Air for Blue Skies")
        elif date == 8:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Literacy Day")
        elif date == 9:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day to Protect Education from Attack")
        elif date == 12:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n United Nations Day for South-South Cooperation")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Democracy")
        elif date == 16:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Preservation of the Ozone Layer")
        elif date == 17:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Patient Safety Day")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Equal Pay Day")
        elif date == 19:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Talk Like a Pirate Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of University Spor")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Peace \n World Alzheimer’s Day \n Biosphere Day")
        elif date == 22:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Rhino Day")
        elif date == 23:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Sign Languages")
        elif date == 24:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Maritime Day")
        elif date == '26':
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Total Elimination of Nuclear Weapons")
        elif date == 27:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Tourism Day")
        elif date == 28:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Awareness of Food Loss and Waste")
        elif date == 29:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Awareness of Food Loss and Waste")
        elif date == 30:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Translation Day \n International Blasphemy Rights Day")
        elif date > 30 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # ocotber
    elif month == 10:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Older Persons")
        elif date == 2:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Non-Violence")
        elif date == 4:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Animal Welfare Day \n World Habitat Day \n World Space Week")
        elif date == 5:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Teachers’ Day \n World Space Week")
        elif date == 6:
            await ctx.send(f"the international days on {date}/{month} are:- \n  World Space Week")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:- \n  World Space Week")
        elif date == 8:
            await ctx.send(f"the international days on {date}/{month} are:- \n  World Space Week")
        elif date == 9:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Post Day \n World Migratory Bird Day \n World Space Week")
        elif date == '10':
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Mental Health Day \n World Migratory Bird Day \n World Space Week")
        elif date == 11:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of the Girl Child")
        elif date == 13:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for Disaster Risk Reduction")
        elif date == 15:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Rural Women")
        elif date == 16:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Food Day")
        elif date == 17:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Eradication of Poverty")
        elif date == 20:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Statistics Day \n International Day of the Air Traffic Controller")
        elif date == 24:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n United Nations Day \n World Development Information Day \n World Polio Day")
        elif date == 27:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Day for Audiovisual Heritage")
        elif date == 30:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Thrift Day")
        elif date == 31:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Cities Day \n Halloween")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # november
    elif month == 11:
        if date == 2:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day to End Impunity for Crimes against Journalists")
        elif date == 5:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Tsunami Awareness Day \n World Day of Romani Language")
        elif date == 6:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for Preventing the Exploitation of the Environment in War and Armed Conflict")
        elif date == 10:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Immunization Day \n World Science Day for Peace and Development")
        elif date == 12:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Pneumonia Day")
        elif date == 13:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Kindness Day ")
        elif date == 14:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Diabetes Day \n International Day against Illicit Trafficking in Cultural Property")
        elif date == 15:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Day of Remembrance for Road Traffic Victims")
        elif date == 16:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day for Tolerance ")
        elif date == 17:
            await ctx.sendd(f"the international days on {date}/{month} are:- \n International Students Day")
        elif date == 18:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Islamic Art")
        elif date == 19:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Toilet Day \n World Philosophy Day \n International Men’s Day")
        elif date == 20:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Africa Industrialization Day \n World Children’s Day \n Transgender Day of Remembrance")
        elif date == 21:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n World Fisheries Day \n World Television Day")
        elif date == 25:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Elimination of Violence against Women \n National Day of Mourning")
        elif date == 26:
            await ctx.send(f"the international days on {date}/{month} are:- \n World Olive Tree Day")
        elif date == 29:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Solidarity with the Palestinian People")
        elif date == 30:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Day of Remembrance for all Victims of Chemical Warfare")
        elif date > 30 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")

    # december
    elif month == 12:
        if date == 1:
            await ctx.send(f"the international days on {date}/{month} are:- \n World AIDS Day ")
        elif date == 2:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day for the Abolition of Slavery")
        elif date == 3:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Persons with Disabilities")
        elif date == 4:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Banks")
        elif date == 5:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Volunteer Day for Economic and Social Development \n World Soil Day")
        elif date == 7:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Civil Aviation Day")
        elif date == 9:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Commemoration and Dignity of the Victims of the Crime of Genocide and of the Prevention of this  \n International Anti-Corruption Day")
        elif date == 10:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n Human Rights Day \n International Animal Rights Day")
        elif date == 11:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Mountain Day")
        elif date == 12:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Neutrality \n International Universal Health Coverage Day")
        elif date == 18:
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Migrants Day \n World Arabic Language Day")
        elif date == 20:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Human Solidarity Day ")
        elif date == 27:
            await ctx.send(f"the international days on {date}/{month} are:- \n International Day of Epidemic Preparedness")
        elif date == 30:
            await ctx.send(f"the international days on {date}/{month} are:- \n 100th anniversary of the ussr(2022) ☭")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")
    else:
        await ctx.send("non existent or non integer month given")


TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
