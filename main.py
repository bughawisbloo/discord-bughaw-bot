import os
import asyncio
import threading
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import app  # Import Flask app

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

# Prefix set to '!' so the command becomes !join1
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def join1(ctx):
    """Command to make this second bot join your current voice channel."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect(reconnect=True, self_deaf=True)
        await ctx.send(f"Joined **{channel.name}**!")
    else:
        await ctx.send("You need to be inside a voice channel first!")

def run_bot():
    """Runs the asyncio event loop for discord.py in a dedicated background thread."""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    token = os.getenv("BOT_TOKEN")
    if token:
        loop.run_until_complete(bot.start(token))
    else:
        print("ERROR: BOT_TOKEN not found in environment variables.")

# Start the Discord bot thread automatically when Gunicorn imports main.py
bot_thread = threading.Thread(target=run_bot, daemon=True)
bot_thread.start()
