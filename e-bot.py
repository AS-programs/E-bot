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
from discord.ext import commands
import randfacts

dotenv.load_dotenv()
client = commands.Bot(command_prefix='$')
client.remove_command('help')

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


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

wordd = [
    'abberation : a departure from what is normal, usual, or expected, typically an unwelcome one\nExample-they described the outbreak of violence in the area as an aberration',
    'abnegation : the action of renouncing or rejecting something \nExample-abnegation of political power',
    'apathetic : showing or feeling no interest, enthusiasm, or concern.\nExample-an apathetic electorate',
    'arbitrary :based on random choice or personal whim, rather than any reason or system\nExample-an arbitrary decision',
    'arduous :involving or requiring strenuous effort; difficult and tiring\nExample-an arduous journey',
    'annex : add (territory) to ones own territory by appropriation\nExample-the left bank of the Rhine was annexed by France in 1797',
    'belittle : dismiss (someone or something) as unimportant\nExample-she belittled his riding skills whenever she could',
    'beguile : charm or enchant (someone), often in a deceptive way.\nExample-he beguiled the voters with his good looks',
    'belligerence : aggressive or warlike behaviour.\nExample-The leaders belligerence is dangerously irresponsible',
    'callous : showing or having an insensitive and cruel disregard for others.\nExample-his callous comments about the murder made me angry',
    'coagulation : the action or process of a liquid, especially blood, changing to a solid or semi-solid state\nExample-a supplement that inhibits blood coagulation',
    'cogent : (of an argument or case) clear, logical, and convincing\nExample-they put forward cogent arguments for British membership',
    'comply : act in accordance with a wish or command\nExample-we are unable to comply with your request',
    'consensus : a general agreement\nExample-there is a growing consensus that the current regime has failed'
    'consign : deliver (something) to a persons keeping.\nExample-he consigned three paintings to Sotheby',
    'construed : interpret (a word or action) in a particular way\nExample-his words could hardly be construed as an apology',
    'contusion : a region of injured tissue or skin in which blood capillaries have been ruptured; a bruise\nExample-a dark contusion on his cheek was beginning to swell',
    'cumbersome : large or heavy and therefore difficult to carry or use; unwieldy.\nExample-cumbersome diving suits',
    'defunct : no longer existing or functioning \nExample - the now defunct Somerset & Dorset railway line',
    'dilatory : slow to act\nExample-he had been dilatory in preparing for his exams',
    'dirge : a mournful song, piece of music, or sound.\nExample-singers chanted dirges',
    'disparate : essentially different in kind; not able to be compared\nExample-they inhabit disparate worlds of thought',
    'dispel : make (a doubt, feeling, or belief) disappear\nExample-The breeze dispelled the bad odor',
    'ecclesiastical : relating to the Christian Church or its clergy\nexample-the ecclesiastical hierarchy',
    'embezzlement : theft or misappropriation of funds placed in ones trust or belonging to ones employer\nExample-charges of fraud and embezzlement',
    'emulate : match or surpass (a person or achievement)\nExample-most rulers wished to emulate Alexander the Great',
    'enervate : make (someone) feel drained of energy or vitality\nExample-the heat enervated us all',
    'enormity : the scale or extent of something percieved as bad or morally wrong\nExample-a thorough search disclosed the full enormity of the crime',
    'equanimity : calmness and composure, especially in a difficult situation\nExample-she accepted both the good and the bad with equanimity',
    'exhort : strongly encourage or urge (someone) to do something\nExample-I exhorted her to be a good child',
    'exigent : pressing; demanding\nExample-the exigent demands of her contemporaries music took a toll on her voice',
    'formidable : inspiring fear or respect through being impressively large, powerful, intense, or capable\nExample-a formidable opponent',
    'gullible : easily persuaded to believe something; credulous.\nExample-an attempt to persuade a gullible public to spend their money',
    'hierarchy : a system in which members of an organization or society are ranked according to relative status or authority\nExample-the initiative was with those lower down in the hierarchy',
    'hoi polloi : the masses; the common people\nExample-the politician decreased the taxes to appease the hoi polloi',
    'ignominious : deserving or causing public disgrace or shame\nExample-no other party risked ignominious defeat',
    'impetuous : acting or done quickly and without thought or care \nExample-she might live to regret this impetuous decision',
    'inane : lacking sense or meaning; silly\nExample-dont badger people with inane questions',
    'inchoate : just begun so not yet fully developed\nExample-a still inchoate democracy',
    'indefatigable : persisting continuosly and tirelessly\nExample-an indefatigable defender of human rights',
    'indict : formally accuse of or charge with a crime\nExample-his former manager was indicted for fraud',
    'infringe : actively break the terms of (a law, agreement, etc.) \nExample-making an unauthorized copy would infringe copyright',
    'inveterate : having a particular habit, activity, or interest that is long-established and unlikely to change\nExample-an inveterate gambler ',
    'martinate : a person who demands complete obedience; a strict disciplinarian\nExample-a martinant dictator ruled the kingdom',
    'mores : the essential or characteristic customs and conventions of a society or community\nExample-an offence against social mores',
    'munificent : characterized by or displaying great generosity\nExample-a munificent bequest',
    'nonplussed : so surprised and confused that one is unsure how to react.\nExample-Henry looked completely nonplussed',
    'noxious : harmful, poisonous, or very unpleasant\nExample-they were overcome by the noxious fumes',
    'obdurate : stubbornly refusing to change ones opinion or course of action\nExample-I argued this point with him, but he was obdurate',
    'paradigm : a typical example or pattern of something,\nExample-The object-oriented paradigm is a new and different way of thinking about programming',
    'phlegmatic : (of a person) having an unemotional and stolidly calm disposition\nExample-the phlegmatic British character',
    'phlogmatic : having an unemotional and stolidly calm disposition\nExample-the phlegmatic British character',
    'portent : a sign or warning that a momentous or calamitous event is likely to happen\nExample-many birds are regarded as being portents of death',
    'potenate : a monarch or ruler, especially an autocratic one\nExample-Valdemar was now, after the king of England, the most powerful potentate in the north of Europe',
    'relegate : assign an inferior rank or position to\nExample-they aim to prevent her from being relegated to a secondary role',
    'remiss : lacking care or attention to duty; negligent\nExample-it would be very remiss of me not to pass on that information',
    'sacrilege : violation or misuse of what is regarded as sacred\nputting ecclesiastical vestments to secular use was considered sacrilege',
    'saguine : optimistic or positive, especially in an apparently bad or difficult situation\nExample-he is sanguine about prospects for the global economy',
    'staid : sedate, respectable, and unadventurous\nExample-staid law firms',
    'toilsome : involving hard or tedious work\nExample-toilsome chores',
    'unabashed : not embarrassed, disconcerted, or ashamed\nExample-he was unabashed despite failing in his test',
    'uncanny : strange or mysterious, especially in an unsettling way\nExample-an uncanny feeling that she was being watched',
    'veracity : conformity to facts; accuracy\nExamples-officials expressed doubts concerning the veracity of the story'

]

microbes = [
    "Rhinovirus\nType:virus\nDisease:Common cold",
    "HIV(Human Immunodeficiency Virus)\nType:virus\nDisease:AIDS(Acquired Immunodeficiency Disease)",
    "Salmonella Typhi\nType:bacteria\nDisease:Typhoid",
    "Vibrio Cholerae\nType:Bacteria\nDisease:Cholera",
    "Bacillus Anthracis\nType:Bacteria\nDisease:Anthrax",
    "Varicella Zoster virus\nType:virus\nDisease:Chickenpox",
    "Yersinia Pestis\nType:bacteria\nDisease:Black Plague",
    "Variola Virus\nType:virus\nDisease:Smallpox",
    "Epstein-Barr virus\nType:virus\nDisease:Mononucleosis",
    "Mycobacterium Tuberculsosis\nType:bacteria\nDisease:Tuberculosis",
    "Rickettsia Rickettsii\nType:bacteria\nDisease:Rocky Mountain Spotted Fever",
    "Bordetella Pertussis\nType:bacteria\nDisease:Whooping Cough",
    "Influenza Virus\nType:virus\nDisease:Flu",
    "Diplocarpon Rosae\nType:fugus\nDisease:Black spot(in plants)",
    "Mosaic Virus\nType:Virus\nDisease:Mosaic disease(in plants)",
    "Plasmodium Malariae\nType:Protozoa\nDisease:Malaria",
    "Dengue Virus\nType:virus\nDisease:Dengue",
    "Cryptospordium\nType:Protozoa\nDisease:Cryptospordiosis",
    "Stachybotrys Chartarum\nType:Fungi\nDisease:Toxic Black Mold(in plants)",
    "Phytophthora Infestans\nType:Fungi\nDisease:Potato Blight(in plants)",
    "Apthovirus\nType:Virus\nDisease:Food and mouth disease(in cattle)",
    "Bluetongue virus\nType:Virus\nDisease:Food and mouth disease(in ruminants)",
    "Clostridium Tetani\nType:Virus\nDisease:Tetanus",
    "Streptococcus Pneumoniae\nType:Bacteria\nDisease:Pneumonia",
    "African Swine Virus\nType:Virus\nDisease:African swine fever",
    "SARS-CoV-2\nType:Virus\nDisease:Covid19",
    "Nipah Virus\nType:Virus\nDisease:Nipah virus infection",
    "Hendra Virus\nType:Virus\nDisease:Hendra virus infection",
    "Mycobacterium Avium\nType:Bacteria\nDisease:Johne's disease(in ruminants)",
    "Erwinia Tracheiphila\nType:Bacteria\nDisease:Bacterial wilt"
]

microbe_images = [
    'images/microbe_images/rhinovirus.png',
    'images/microbe_images/hiv.png',
    'images/microbe_images/salmonellatyphi.png',
    'images/microbe_images/vibrio_cholerae.png',
    'images/microbe_images/bacillus_anthracis.png',
    'images/microbe_images/varicella_zoster.png',
    'images/microbe_images/yersinia_pestis.png',
    'images/microbe_images/variola_virus.png',
    'images/microbe_images/epstein_virus.png',
    'images/microbe_images/mycoacterium_tuberculosis.png',
    'images/microbe_images/rickettsia_rickettsii.png',
    'images/microbe_images/bordetella_pertusis.png',
    'images/microbe_images/influenza.png',
    'images/microbe_images/blackspot.png',
    'images/microbe_images/mosaicvirus.png',
    'images/microbe_images/Plasmodiummalariae.jpg',
    'images/microbe_images/Denguevirus.jpg',
    'images/microbe_images/cryptosporidiummuris.jpg',
    'images/microbe_images/stachybotrys.jpg',
    'images/microbe_images/phytophthora_infestans.jpg'
    'images/microbe_images/apthovirus.jpg',
    'images/microbe_images/bluetonguevirus.jpg',
    'images/microbe_images/clostridium.jpg',
    'images/microbe_images/streptococcuspneumoniae.jpg',
    'images/microbe_images/africanswinefevervirus.jpg',
    'images/microbe_images/covid19.jpg',
    'images/microbe_images/nipahvirus.jpg',
    'images/microbe_images/hendravirus.jpg',
    'images/microbe_images/mycobacteriumavium.jpg',
    'images/microbe_images/erwiniatracheiphila.jpg'
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

sourcee = [
    'source - mind your decisions (youtube)',
    'source - michael penn (youtube)',
    'source - michael penn (youtube)',
    'source - general question',
    'source - some math textbook',
    'source - michael penn (youtube)',
    'source - some math textbook',
    'source - professor dave explains (youtube)',
    'source - general',
    'source - professor dave explains (youtube)',
    'source - professor dave explains (youtube)',
    'source - professor dave explains (youtube)',
    'source - michael penn (youtube)',
    'source - professor dave explains(youtube)',
    'source - numberphile',
    'source - professor dave explains(youtube)',
    'source - Atomi(youtube)',
    'source = Atomi(youtube)'
]

math_probs = [
    'images/math_probs/koink.png',
    'images/math_probs/koinktwo.png',
    'images/math_probs/koinkthree.png',
    'images/math_probs/koinkfour.png',
    'images/math_probs/koinkfive.png',
    'images/math_probs/koinksix.png',
    'images/math_probs/koinkseven.png',
    'images/math_probs/koinkeight.png',
    'images/math_probs/koinknine.png',
    'images/math_probs/koinkten.png',
    'images/math_probs/koinkeleven.png',
    'images/math_probs/koinktwelve.png',
    'images/math_probs/koinkthirteen.png',
    'images/math_probs/koinkfourteen.png',
    'images/math_probs/koinkfifteen.png',
    'images/math_probs/koinksixteen.png',
    'images/math_probs/koinkseventeen.png',
    'images/math_probs/koinkeighteen.png'
]


math_answers=[
    'answer- ||90 ||',
    'answer - ||n=2,3||',
    'answer - ||12-4e||',
    'answer - ||π     ||',
    'answer - ||root π||',
    'answer - ||ln(e^x/(e^x+1))||',
    'answer - ||x= 1 or -1||',
    'answer - ||18      ||',
    'answer - ||~0.916 (catalans constant)||',
    'answer - ||(56/5)π||',
    'answer - ||144.36  ||',
    'answer - ||45/2    ||',
    'answer - ||there are no solutions||',
    'answer - ||0.22%||',
    'answer - ||the question is wrong(see Bertrands Paradox):wink:||',
    'answer - ||22/15||',
    'answer - ||tan x ||',
    'answer - ||√2(√3-1)/4 ||'
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
async def hello(ctx):
    await ctx.send(random.choice(hello_words))


@client.command()
async def inspire(ctx):
    quote = get_quote()
    await ctx.send(quote)


@client.command()
async def word(ctx):
    await ctx.send(random.choice(wordd))


@client.command()
async def microbe(ctx):
    x = len(microbes)
    y = random.randint(0, x - 1)
    await ctx.send(microbes[y])
    await ctx.send(file=discord.File(microbe_images[y]))


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
    await ctx.send("$add/subtract/multiply/divide/exponent/gcd/lcm <number 1> <number 2>\n$randnum <number1> <number2> (for example- ``$randnum 5 10`` gives a random number between 5 and 10)(both numbers should be integers)\n$factorial <number> \ntrigonometry comands - $cos/sin/tan/cot/cosec/sec/cosh/sinh/tanh/acos/asin/atan <number>(works in radians)\n$mathprob(gives a random math problem)\n$mathsymbols(gives a list of mathsymbols)")


@client.command()
async def mathprob(ctx):
    x = len(math_probs)
    y = random.randint(0, x - 1)
    await ctx.send(sourcee[y])
    await ctx.send(file=discord.File(math_probs[y]))
    await ctx.send(math_answers[y])


@client.command()
async def mathsymbols(ctx):
    await ctx.send("± - plus or minus symbol\nΦ - phi\n≅ - congruency\n≠ - not equal\n° - degree\n× - vector product sign\n÷ - division sign\n≠ - not equal to\n≥,≤,>,< - inequality\n√ - square root \n∝ - proportionality symbol\nφ - golden ratio constant\nε -  Epsilon\ne-euler's number\nℵo-aleph null\ni-imaginary number\ny', y'', dy/dx , ∂/∂x - derivative\n∫ , ∬ , ∭ ,∮ , ∯ , ∰  - integral \n∇ - delta\nδ - delta function\n∞-infinity symbol\nω - omega\nℱ - fourier tranform\n⋂,⋃,⊆,⊂,⊄,⊇,⊃,⊅,Ø,⇒,∀,∃,∄,∴,∵ - set symbols\nℒ - Laplace tranform\nΣ - sigma notation symbol\nπ - pi\nα - alpha\nβ - beta\nγ - gamma\nθ - theta\nΨ - psi\nΩ - omega\nζ(s) - Riemann zeta function")

@client.command()
async def lcm(ctx, x: int, y: int):
    await ctx.send(lcmm(x,y))


@client.command()
async def gcd(ctx, x: int, y: int):
    await ctx.send(gcdd(x,y))


@client.command()
async def factorial(ctx, x: int):
    while True:
        try:
          await ctx.send(factoriall(x))
          break
        except OverflowError:
            await ctx.send("whoops,factorial too high")
            break


@client.command()
async def add(ctx, x: float, y: float):
    await ctx.send(x + y)


@client.command()
async def subtract(ctx, x: float, y: float):
    await ctx.send(x - y)


@client.command()
async def multiply(ctx, x: float, y: float):
    await ctx.send(x * y)


@client.command()
async def divide(ctx, x: float, y: float):
    while True:
        try:
            await ctx.send(x / y)
            break
        except ZeroDivisionError:
            await ctx.send("that is not defined :|")
        break


@client.command()
async def exponent(ctx, x: float, y: float):
    while True:
        try:
            await ctx.send(x ** y)
            break
        except OverflowError:
            await ctx.send("exponent too high :|")
            break


@client.command()
async def cos(ctx, x: float):
    await ctx.send(meth.cos(x))


@client.command()
async def sin(ctx, x: float):
    await ctx.send(meth.sin(x))


@client.command()
async def tan(ctx, x: float):
    await ctx.send(meth.tan(x))


@client.command()
async def sec(ctx, x: float):
    await ctx.send(1 / meth.cos(x))


@client.command()
async def cosec(ctx, x: float):
    await ctx.send(1 / meth.sin(x))


@client.command()
async def cot(ctx, x: float):
    await ctx.send(1 / meth.tan(x))

@client.command()
async def cosh(ctx, x: float):
    await ctx.send(meth.cosh(x))

@client.command()
async def acos(ctx, x: float):
    await ctx.send(meth.acos(x))

@client.command()
async def asin(ctx, x: float):
    await ctx.send(meth.asin(x))

@client.command()
async def sinh(ctx, x: float):
    await ctx.send(meth.sinh(x))

@client.command()
async def tanh(ctx, x: float):
    await ctx.send(meth.atan(x))

@client.command()
async def atan(ctx, x: float):
    await ctx.send(meth.tanh(x))

@client.command()
async def randnum(ctx, x: float, y: float):
    await ctx.send(random.randint(x, y))


@client.command()
async def extras(ctx):
    await ctx.send("$source - shows some of the sources for the commands\n$bot - gives basic info about the bot\n$update-shows the recent updates for the bot")


@client.command()
async def source(ctx):
    await ctx.send("$word-English Oxford Dictionary\n$fact-Randfacts package\nmicrobes images-mostly wikipedia\nevents-https://www.gkgigs.com/important-world-international-days/")

@client.command()
async def bot(ctx):
    hm=len(math_probs)
    hmm=len(wordd)
    hmmm=len(microbes)
    await ctx.send(f"Hello i am e-bot\ni was made in python (discord.py)\nnumber of mathproblems for mathprob command - {hm}\nnumber of words in word command - {hmm}\nnumber of microbes in microbe command - {hmmm}")

@client.command()
async def update(ctx):
    await ctx.send(f"added a math symbol\n-developer of e bot(on 03/02/2022)")


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
            await ctx.send(
                f"the international days on {date}/{month} are:- \n International Day of Epidemic Preparedness")
        elif date > 31 or date < 0:
            await ctx.send("no such dates exist in the given month")
        else:
            await ctx.send(f"no inportant international days on {date}/{month}")
    else:
        await ctx.send("non existent or non integer month given")


TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
