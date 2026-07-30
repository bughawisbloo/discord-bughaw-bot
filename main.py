import os
import discord
from discord.ext import commands
from keep_alive import keep_alive  # <--- Add this import

keep_alive()  # <--- Start web server

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# ... your bot logic ...

bot.run(os.getenv("BOT_TOKEN"))