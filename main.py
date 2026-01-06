import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import random

from spirits.wisdom import wisdom
from spirits.visions import visions
from spirits.animals import animals

load_dotenv()  # Das bleibt jetzt fest im Code
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Token aus der Umgebungsvariable lesen
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise RuntimeError(
        "Fehler: Bitte setze die Umgebungsvariable DISCORD_TOKEN!")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Spirit Bot online als {bot.user}")

# 🪶 Weisheit


@bot.tree.command(name="weisheit", description="Die Geister sprechen zu dir.")
async def weisheit(interaction: discord.Interaction):
    text = random.choice(wisdom)
    await interaction.response.send_message(f"🪶 **Die Geister flüstern:**\n{text}")

# 🐺 Geisttier


@bot.tree.command(name="geistertier", description="Ein Geisttier zeigt sich.")
async def geistertier(interaction: discord.Interaction):
    tier, bedeutung = random.choice(list(animals.items()))
    await interaction.response.send_message(
        f"🐺 **Dein Geisttier ist: {tier}**\nBedeutung: *{bedeutung}*"
    )

# 🔮 Vision


@bot.tree.command(name="vision", description="Eine Vision offenbart sich!")
async def vision(interaction: discord.Interaction):
    text = random.choice(visions)
    await interaction.response.send_message(f"🔮 **Vision:**\n{text}")

# Rituale


@bot.command()
async def rituals(ctx, name: str = None):
    # Prüfen, ob ein Name eingegeben wurde
    if name is None:
        return await ctx.send(f"❌ **Meines wissen nicht, welches Ritual du meinst.**\nBitte schreibe: `/rituals [Name]` (z.B. `/rituals blutmond`)")

    # Name in Kleinschreibung umwandeln für den Abgleich im Dictionary
    name = name.lower()

    if name in rituals:
        r = rituals[name]

        # Den Text aus dem Dictionary zusammenbauen
        ritual_text = f"✨ **{r['name']}** ✨\n"
        ritual_text += f"📜 *{r['beschreibung']}*\n\n"

        for schritt in r['schritte']:
            ritual_text += f"{schritt}\n"

        await ctx.send(ritual_text)
    else:
        # Falls das Ritual nicht im Dictionary 'rituale' existiert
        await ctx.send(f"❌ **Meines kennen dieses Ritual nicht.** Hast du dich verschrieben? Meines kennen nur: `{', '.join(rituals.keys())}`")

bot.run(DISCORD_TOKEN)
