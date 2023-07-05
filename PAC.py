import discord
import discord.ext
from discord import Intents
from discord.ext import commands
from discord import app_commands
import openai

openai.api_key = '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'

intents = discord.Intents.all()
intents.typing = False  # Опционально, чтобы отключить набор сообщений ботом
intents.presences = False

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=966719758273769472))
    print(f'Бот {client.user} подключился к серверу')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!PacAI'):
        user_input = message.content[len('!PacAI'):].strip()
        
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=4000,
            temperature=0.7,
            n=1,
            stop=None,
        )
        
        await message.channel.send(response.choices[0].text.strip())
    if message.content.startswith('!clear'):
        await clear_channel(message.channel)

async def clear_channel(channel):
    async for message in channel.history(limit=None):
        await message.delete()
    
client.run('MTEyNDE4OTI2MTYyNTgzOTYxNg.GKLtgw.hMCNZ64-edAUaZXnYRO4pREn6_WiFHsb5mon7Y')