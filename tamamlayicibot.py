import discord
from discord.ext import commands
from discord.utils import get
import random
from random import randrange
import time
import youtube_dl
from youtube_dl import YoutubeDL
import asyncio
import nacl


yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)
ffmpeg_options = {'options': '-vn'}

intents = discord.Intents.default()
client = commands.Bot(command_prefix = "!",intents=intents)


intents.message_content = True
intents.members = True


@client.event
async def on_ready():
    print('{0.user} is Live'
    .format(client))
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("!yardim"))


client.deleteToggle: bool = True


niCuss = ["KUFURLERIN"]
inaCuss = ["KUFURLERIN"]
inCuss = ["KUFURLERIN"]



@client.event
async def on_message(message):
    niCussRandom = random.choice(niCuss)
    inaCussRandom = random.choice(inaCuss)
    inCussRandom = random.choice(inCuss)

    outta5 = randrange(5)

    if message.author == client.user:
        return
        

    if message.content[-2:] == "ni" or message.content[-2:] == "nı" or message.content[-2:] == "nu":
        if client.deleteToggle == True:
            await message.channel.purge(limit=1)
            time.sleep(0.5)
        await message.channel.send(f"{message.content} {niCussRandom}")
        if outta5 == 1:
            time.sleep(0.5)
            await message.channel.send("...")
            time.sleep(0.5)
            await message.channel.send("tamam mı?")

    if message.content[-3:] == "ine" or message.content[-3:] == "ina" or message.content[-3:] == "una":
        await message.channel.send(f"{message.content} {inaCussRandom}")
        if client.deleteToggle == True:
            await message.channel.purge(limit=1)
            time.sleep(0.5)
        if outta5 == 1:
            time.sleep(0.5)
            await message.channel.send("...")
            time.sleep(0.5)
            await message.channel.send("tamam mı?")

    if message.content[-2:] == "in" or message.content[-2:] == "ın" or message.content[-2:] == "nu":
        await message.channel.send(f"{message.content} {inCussRandom}")
        if client.deleteToggle == True:
            await message.channel.purge(limit=1)
            time.sleep(0.5  )
        if outta5 == 1:
            time.sleep(0.5)
            await message.channel.send("...")
            time.sleep(0.5)
        await message.channel.send("tamam mı?")



    await client.process_commands(message)


@client.command(pass_context=False)
async def yardim(ctx):
    if client.deleteToggle == True:
        await ctx.channel.purge(limit=1)
    await ctx.send("```Yardim Komutlari:\n!sik\n!sil\n!ben\n!faktoriyel\n!bcs\nAyrica kufurlu cumlelerinin tamamlanmasini istiyorsan, cumleyi kufur ile bitirmeden gondermen yeterli.```")

@client.command()
async def sil(ctx):
    client.deleteToggle = not client.deleteToggle
    if client.deleteToggle:
        await ctx.send("Mesajlar, ben isimi gorukten sonra silinecektir...")
    else:
        await ctx.send("Mesajları silmemek durumundayim 8===D.")

@client.command()
async def factorial(ctx, number: int):
    if client.deleteToggle == True:
        await ctx.channel.purge(limit=1)
    outnum = 1
    for i in range(1, number+1):
        outnum *= i 
    await ctx.send(f"Sayının Faktoriyeli: {outnum}")


@client.command()
async def ben(ctx):
    tags = [f"tam bir orospu çocuğu", "agzinda gezdiren", "götten yemiş", "anası sikik", "sıfatı kusturtan", "beyinsiz", "kitapı sikik"]
    if client.deleteToggle == True:
        await ctx.channel.purge(limit=1)
    tagRandom = random.choice(tags)
    tagRandom2 = random.choice(tags)
    while True:
        if tagRandom2 == tagRandom:
            tagRandom2 = random.choice(tags)
        else:
            break
    await ctx.send(f"Ben {tagRandom}, {tagRandom2} {ctx.author.name}.")


voice_clients = {}
gifs = ["https://tenor.com/view/better-call-saul-loop-3d-edit-gif-24518425", "https://media.discordapp.net/attachments/697789051755036715/1011357059142393916/better-ball-saul-better-call-saul.gif", "https://tenor.com/view/saul-goodman-better-call-soul-gif-12217792", "https://tenor.com/view/afham-saul-goodman-better-call-saul-bob-odenkirk-jimmy-mcgill-gif-25559831"]

@client.command(pass_context =True)
async def bcs(ctx):
    if client.deleteToggle == True:
        await ctx.channel.purge(limit=1)
    try:
        
        if (ctx.author.voice):
            url = "https://www.youtube.com/watch?v=yBm4K00SMEk"
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\Users\\boran\\OneDrive\\Masaüstü\\ffmpeg\\ffmpeg.exe")
            channel = ctx.message.author.voice.channel
            voice_clients[ctx.guild.id] = channel
            voice = get(client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected:
                await voice.move_to(channel)
            else:
                conn = await channel.connect()
                conn.play(player)
        else:
            await ctx.send(f"Konusmada olmadigin icin maalesef sadece gif ile yetineceksin {ctx.author.name} ...")
    except Exception as err:
        print(err)
    

    await ctx.send(random.choice(gifs))
    time.sleep(18.5)
    await ctx.guild.voice_client.disconnect()


@client.command()
async def sik(ctx, message: int):
    if message > 0:
        await ctx.channel.purge(limit= message+1)
        time.sleep(.1) 
        await ctx.send(f"{message} mesaj sikildi.")

client.run("YOUR TOKEN")

