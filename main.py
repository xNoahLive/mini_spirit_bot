import discord
from discord.ext import commands
from discord import app_commands
import random

from config import DISCORD_TOKEN
from spirits.wisdow import wisdow
from spirits.visions import visions
from spirits.animals import animals

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Spirit Bot online als {bot.user}")

# 🪶 Weisheit


@bot.tree.command(name="weisheit", description="Die Geister sprechen zu dir.")
async def weisheit(interaction: discord.Interaction):
    text = random.choice(wisdow)
    await interaction.response.send_message(f"🪶 **Die Geister flüstern:**\n{text}")

# 🐺 Geisttier


@bot.tree.command(name="geistertier", description="Dein Geisttier zeigt sich.")
async def geistertier(interaction: discord.Interaction):
    tier, bedeutung = random.choice(list(animals.items()))
    await interaction.response.send_message(
        f"🐺 **Dein Geisttier ist der {tier}**\nBedeutung: *{bedeutung}*"
    )

# 🔮 Vision


@bot.tree.command(name="vision", description="Eine Vision offenbart sich.")
async def vision(interaction: discord.Interaction):
    text = random.choice(visions)
    await interaction.response.send_message(f"🔮 **Vision:**\n{text}")

bot.run(DISCORD_TOKEN)
