
import discord
#from discord import Embed, Game
#from discord.ext import menus
#from discord.ext.commands import Bot, has_guild_permissions
#from discord.ext.commands.errors import CommandNotFound
#from discord.utils import find
#from dotenv import load_dotenv
from discord.ext import commands
import pandas as pd

client = discord.Client()

Characters = ["ssjgoku","ssvegeta","teengohan","krillin","piccolo","yamcha","adultgohan","gotenks","tien","ssbgoku","ssbvegeta","baseku","bardock"
              "ssbvegito","ssbgogeta","android17","videl","roshi","gtgoku","uigoku","a21lc","cell","ss4gogeta","frieza","android18","majinbuu"
              "kidbuu","android16","beerus","ginyu","android21","hit","nappa","gokublack","zbroly","basevegeta","cooler","zamasu","dbsbroly"
              "janemba","jiren","superbaby2","kefla"
              ]



@client.event # Basic command to login the bot
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

bot = commands.Bot(command_prefix='$')
@client.event

async def on_message(message):

    Message = message.content

    def findchar(string):  # Find character name in Database
        index = 0
        for item in Characters:
            try:
                if string.find(Characters[index]) != -1:
                    string = Characters[index].lower()
                    return string
                else:
                    index = index + 1
            except:
                pass

    def findattack(string):  # Find attack input in Database
        string = set(string.split()) & set(attacklist)
        Convertlist = list(string)
        return Convertlist[0]

    def Colorbychar(string):
        if string == "ssjgoku":
            return 0xfff700
        if string == "ssvegeta":
            return 0xe6df0a
        if string == "teengohan":
            return 0xa00ae6
        if string == "krillin":
            return 0xa00ae6
        if string == "piccolo":
            return 0x970fd7
        if string == "yamcha":
            return 0xdb8f0a
        if string == "gotenks":
            return 0xfff700
        if string == "tien":
            return 0x03021d
        if string == "ssbgoku":
            return 0x0de4e7
        if string == "ssbvegeta":
            return 0x0de4e7
        if string == "baseku":
            return 0xdb8f0a
        if string == "bardock":
            return 0x7f0a0a
        if string == "ssbvegito":
            return 0x0de4e7
        if string == "ssbgogeta":
            return 0x0de4e7
        if string == "android17":
            return 0x165e08
        if string == "videl":
            return 0xa80efb
        if string == "roshi":
            return 0xe3e3e3
        if string == "gtgoku":
            return 0x47609a
        if string == "uigoku":
            return 0xcfd2d8
        if string == "a21lc":
            return 0xc67324
        if string == "cell":
            return 0x1e8410
        if string == "ss4gogeta":
            return 0xda0b0b
        if string == "frieza":
            return 0x8401ef
        if string == "android18":
            return 0x022bf7
        if string == "majinbuu":
            return 0xfe86f4
        if string == "kidbuu":
            return 0xfe86f4
        if string == "android16":
            return 0x116510
        if string == "beerus":
            return 0x641065
        if string == "ginyu":
            return 0x8401ef
        if string == "android21":
            return 0xfe86f4
        if string == "hit":
            return 0x641065
        if string == "nappa":
            return 0xb6a811
        if string == "zbroly":
            return 0xec276c
        if string == "gokublack":
            return 0xff0059
        if string == "basevegeta":
            return 0xb6a811
        if string == "cooler":
            return 0x9900ff
        if string == "zamasu":
            return 0x149935
        if string == "dbsbroly":
            return 0xec276c
        if string == "janemba":
            return 0x991414
        if string == "jiren":
            return 0xc70505
        if string == "superbaby2":
            return 0xece404
        if string == "kefla":
            return 0x1ce358


    def CharacterFullName(string):
        if string == "ssjgoku":
            return "Goku Super Saiyan"
        if string == "ssvegeta":
            return "Vegeta Super Saiyan"
        if string == "teengohan":
            return "Gohan Super Saiyan 2"
        if string == "krillin":
            return "Krillin"
        if string == "piccolo":
            return "Piccolo"
        if string == "yamcha":
            return "Yamcha"
        if string == "gotenks":
            return "Super Saiyan 3 Gotenks"
        if string == "tien":
            return "Tien"
        if string == "ssbgoku":
            return "Super Saiyan Blue Goku"
        if string == "ssbvegeta":
            return "Super Saiyan Blue Vegeta"
        if string == "baseku":
            return "Base Form Goku"
        if string == "bardock":
            return "Bardock"
        if string == "ssbvegito":
            return "Super Saiyan Blue Vegito"
        if string == "ssbgogeta":
            return "Super Saiyan Blue Gogeta"
        if string == "android17":
            return "Android 17"
        if string == "videl":
            return "Videl"
        if string == "roshi":
            return "Master Roshi"
        if string == "gtgoku":
            return "GT Goku"
        if string == "uigoku":
            return "Ultra Instinct Goku"
        if string == "a21lc":
            return "Android 21(Lab Coat)"
        if string == "cell":
            return "Perfect Form Cell"
        if string == "ss4gogeta":
            return "Super Saiyan 4 Gogeta"
        if string == "frieza":
            return "Frieza"
        if string == "android18":
            return "Android 18"
        if string == "majinbuu":
            return "Majin Buu"
        if string == "kidbuu":
            return "Kid Buu"
        if string == "android16":
            return "Android 16"
        if string == "beerus":
            return "God of Destruction Beerus"
        if string == "ginyu":
            return "Captain Ginyu"
        if string == "android21":
            return "Android 21"
        if string == "hit":
            return "Hit"
        if string == "nappa":
            return "Nappa"
        if string == "zbroly":
            return "Legendary Super Saiyan Broly"
        if string == "gokublack":
            return "Super Saiyan Rose Goku Black"
        if string == "basevegeta":
            return "Base Vegeta"
        if string == "cooler":
            return "Cooler"
        if string == "zamasu":
            return "Fused Zamasu"
        if string == "dbsbroly":
            return "DBS Broly"
        if string == "janemba":
            return "Janemba"
        if string == "jiren":
            return "Jiren the Grey"
        if string == "superbaby2":
            return "Super Baby 2"
        if string == "kefla":
            return "Kefla"

    def CharacterThumbNail(string):
        if string == "ssjgoku":
            return "https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png"
        if string == "ssvegeta":
            return "https://cdn.discordapp.com/attachments/1004471658133860513/1004489315256115302/54px-DBFZ_SS_Vegeta_Icon.png"
        if string == "teengohan":
            return "https://cdn.discordapp.com/attachments/770325765467275367/1004521831648202832/65px-DBFZ_Teen_Gohan_Icon.png"




    if message.author == client.user:
        return

    if Message.lower().startswith(".dbfz") and any(word in Message.lower().split() for word in Characters):
        Character = findchar(Message.lower())
        data = pd.read_csv("Database/{}.csv".format(Character), index_col=0)  # Get the right database for Character
        attacklist = data['input'].tolist()  # Make list of possible attacks from input
        for item in range(len(attacklist)):
            attacklist[item] = attacklist[item].upper()
        if any(item in Message.upper().split() for item in attacklist):
            Attack = findattack(Message.upper())
            embed = discord.Embed(title=CharacterFullName(Character.lower()), description="", color=Colorbychar(Character.lower()))
            #embed.set_author(name="DBFZGoku", icon_url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
            #.set_thumbnail(url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
            #embed.set_thumbnail(url=CharacterThumbNail(Character.lower()))
            #embed.set_image(url=data[data["input"] == Attack]['image'].values[0])
            #embed.add_field(name="index", value=data[data["input"] == Attack]['index'].values[0], inline=True)
            embed.add_field(name="input", value=data[data["input"] == Attack]['input'].values[0], inline=True)
            embed.add_field(name="name", value=data[data["input"] == Attack]['name'].values[0], inline=True)
            embed.add_field(name="damage", value=data[data["input"] == Attack]['damage'].values[0], inline=True)
            embed.add_field(name="smash", value=data[data["input"] == Attack]['smash'].values[0], inline=True)
            embed.add_field(name="prorate", value=data[data["input"] == Attack]['prorate'].values[0], inline=True)
            embed.add_field(name="guard", value=data[data["input"] == Attack]['guard'].values[0], inline=True)
            embed.add_field(name="startup", value=data[data["input"] == Attack]['startup'].values[0], inline=True)
            embed.add_field(name="active", value=data[data["input"] == Attack]['active'].values[0], inline=True)
            embed.add_field(name="recovery", value=data[data["input"] == Attack]['recovery'].values[0], inline=True)
            embed.add_field(name="onBlock", value=data[data["input"] == Attack]['onBlock'].values[0], inline=True)
            embed.add_field(name="invuln", value=data[data["input"] == Attack]['invuln'].values[0], inline=True)
            embed.add_field(name="level", value=data[data["input"] == Attack]['level'].values[0], inline=True)
            embed.add_field(name="blockstun", value=data[data["input"] == Attack]['blockstun'].values[0], inline=True)
            embed.add_field(name="groundHit", value=data[data["input"] == Attack]['groundHit'].values[0], inline=True)
            embed.add_field(name="airHit", value=data[data["input"] == Attack]['airHit'].values[0], inline=True)
            await message.channel.send(embed=embed)
        elif Message.lower().startswith(".dbfz"):# and any(word not in Message.lower().split() for word in Characters):
            embed = discord.Embed(color=0xff0000)
            embed.set_author(name="DBFZGoku",icon_url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
            embed.add_field(name="Your character's [Attack] wasn't found in the database.",value="Please use: .dbfz [Name] [Attack]", inline=False)
            embed.add_field(name="For additional help you can use", value=".dbfz", inline=False)
            await message.channel.send(embed=embed)
    elif Message.lower().startswith(".dbfz"):
        embed = discord.Embed(color=0xff0000)
        embed.set_author(name="DBFZGoku",icon_url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1004471796239700028/1004471825033593022/65px-DBFZ_SS_Goku_Icon.png")
        embed.add_field(name="Your character's [Name] wasn't found in the database.",value="Please use: .dbfz [Name] [Attack]", inline=False)
        embed.add_field(name="For additional help you can use", value=".dbfz", inline=False)
        await message.channel.send(embed=embed)

#if message.lower.starts

Token = "OTc5NjkxNzAzMTYwMTY4NDg5.GDqidV.2aGmKRz0hQ5DVNeCD9AnEH3GX28ZlhOYb_NTg8"
client.run(Token)