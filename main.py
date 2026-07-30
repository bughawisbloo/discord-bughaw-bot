import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from keep_alive import app, keep_alive  # <--- Import 'app' here

load_dotenv()

# Start background Flask server thread
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect(reconnect=True, self_deaf=True)
        await ctx.send(f"Joined {channel.name}!")
    else:
        await ctx.send("You need to be in a voice channel first!")

# Only run bot.run() directly when executing main.py
if __name__ == "__main__":
    TOKEN = os.getenv("BOT_TOKEN")
    if TOKEN:
        bot.run(TOKEN)
