import discord
import discord.ext
from discord import Intents
from discord.ext import commands
from discord import app_commands
import openai

openai.api_key = 'chatgpt_api_key'

intents = discord.Intents.all()
intents.typing = False  # Опционально, чтобы отключить набор сообщений ботом
intents.presences = False

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_discord_api))
    print(f'Бот {client.user} подключился к серверу')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('! NameCommand'):
        user_input = message.content[len('! NameCommand'):].strip()
        
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=2000,
            temperature=0.7,
            n=1,
            stop=None,
        )
        
        await message.channel.send(response.choices[0].text.strip())
    
client.run('discord_bot_api_key')
