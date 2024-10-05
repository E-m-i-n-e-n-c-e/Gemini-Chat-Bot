import discord
from discord.ext import commands
from config import DISCORD_API_TOKEN
from Cogs.GeminiCog import GeminiAgent
import asyncio
import utils.commandslist as commandslist  # Import the commands module
import utils.events as events  # Import the events module

# Simulated persistent storage
default_categories = {
    'voice': None,
    'text': None
}

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), help_command=None)

# Load commands and events
commandslist.setup(bot, default_categories)
events.setup(bot)

async def startcogs():
    await bot.add_cog(GeminiAgent(bot))

asyncio.run(startcogs())

bot.run(DISCORD_API_TOKEN)
