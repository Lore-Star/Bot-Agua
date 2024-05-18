import discord
from discord.ext import commands
from token1 import token


intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def tip1(message):
    await message.send('Tomate duchas más cortas')

@bot.command()
async def tip2(message):
    await message.send('No tires basura al mar', file=discord.File('tarea xd/images/3.png'))

@bot.command()
async def tip3(message):
    await message.send('No uses el retrete como un bote de basura', file=discord.File('tarea xd/images/2.png'))

@bot.command()
async def definicion(message):
    await message.send('Para poder entender las funciones del agua, su composición y el ciclo, primero debemos definir qué es el agua: se trata de una sustancia cuyas moléculas están compuestas por un átomo de oxígeno y dos de hidrógeno. Es un líquido inodoro –no tiene olor–, insípido –no tiene sabor– e incoloro –sin color–.', file=discord.File('tarea xd/images/1.jpeg'))

bot.run(token)