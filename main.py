import discord #credit to Rapptz on github for the discord.py library, allows me to manipulate discord bots
import asyncio #credit to Python for the impletmented asyncio library 
from discord.ext import commands #credit to Rapptz on github for the discord.py library, allows me to manipulate discord bots
import random #credit to Python for the impletmented random library 


bot = commands.Bot("")


moods = ["Depressed", "Bubbly", "Sad", "Discouraged", "Angry", "Cheerful", "Energetic", "Empowered", "Annoyed", "Tense"]

encouragement_music = ["https://www.youtube.com/watch", #credit to Pharrell Williams for the music 
"https://www.youtube.com/watch?v=Gs069dndIYk&list=RDQMhH0aPyl", #credit to Earth Wind & Fire for the music
"https://www.youtube.com/watch?v=09R8_2nJtjg", #credit to Maroon 5 for the music
"https://www.youtube.com/watch?v=KQ6zr6kCPj8&list=RDQMh", #credit to LMFAO for the music
"https://www.youtube.com/watch?v=AgFeZr5ptV", #credit to Taylor Swift for the music
"https://www.youtube.com/watch?v=ru0K8uYEZWw&list=PLAQ7nLSEnhWTEihjeM1I-ToPDJEKfZHZu&index=22"] #credit to Justin Timberlake

@bot.event
async def on_ready():
    print("Ready!")



@bot.event
async def on_message(message):
    if message.content.startswith('-help'):
        await message.channel.send("Mood words: Depressed, Sad, Discouraged, Angry, Cheerful, Energetic, Empowered, Annoyed, Tense. Input any of these to get the corresponding music!")
    elif message.content.startswith('-exit'):
      await message.channel.send("You have exited the program! Type in '-help' to restart!")
      exit
    i = 0
    while i < len(moods):
      for i in moods:
        if message.content.startswith(i):
          await message.channel.send(random.choice(encouragement_music))
          i += 1
      
      







on_message('-help')
bot.run("NjM1OTEyOTM2MjQ1ODIxNDU3.Xa3-Eg.HMOgekAuvBZifbyx5ShkcdOp8Pc", bot=True) #discord bots run
