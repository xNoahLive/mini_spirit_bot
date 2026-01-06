# import os
# from dotenv import load_dotenv
# import discord
# from discord.ext import commands
# from discord import app_commands
# import random

# from spirits.wisdom import wisdom
# from spirits.visions import visions
# from spirits.animals import animals
# from spirits.rituals import rituale

# load_dotenv()  # Das bleibt jetzt fest im Code
# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# # Token aus der Umgebungsvariable lesen
# DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# if not DISCORD_TOKEN:
#     raise RuntimeError(
#         "Fehler: Bitte setze die Umgebungsvariable DISCORD_TOKEN!")

# intents = discord.Intents.default()
# bot = commands.Bot(command_prefix="!", intents=intents)


# @bot.event
# async def on_ready():
#     await bot.tree.sync()
#     print(f"Spirit Bot online als {bot.user}")

# # 🪶 Weisheit


# @bot.tree.command(name="weisheit", description="Die Geister sprechen zu dir.")
# async def weisheit(interaction: discord.Interaction):
#     text = random.choice(wisdom)
#     await interaction.response.send_message(f"🪶 **Die Geister flüstern:**\n{text}")

# # 🐺 Geisttier


# @bot.tree.command(name="geistertier", description="Ein Geisttier zeigt sich.")
# async def geistertier(interaction: discord.Interaction):
#     tier, bedeutung = random.choice(list(animals.items()))
#     await interaction.response.send_message(
#         f"🐺 **Dein Geisttier ist: {tier}**\nBedeutung: *{bedeutung}*"
#     )

# # 🔮 Vision


# @bot.tree.command(name="vision", description="Eine Vision offenbart sich!")
# async def vision(interaction: discord.Interaction):
#     text = random.choice(visions)
#     await interaction.response.send_message(f"🔮 **Vision:**\n{text}")

# # Rituale


# @bot.tree.command(name="rituals", description="Zeigt die Schritte für ein heiliges Ritual.")
# @app_commands.describe(name="Welches Ritual? (z.B. blutmond, reinigung)")
# async def rituals(interaction: discord.Interaction, name: str = None):
#     # Wenn kein Name eingegeben wurde
#     if name is None:
#         keys = ", ".join(rituale.keys())
#         return await interaction.response.send_message(
#             f"❌ **Meines wissen nicht, welches Ritual du meinst.**\nBitte wähle: `{keys}`",
#             ephemeral=True
#         )

#     name_lower = name.lower()

#     if name_lower in rituale:
#         r = rituale[name_lower]

#         # Text zusammenbauen
#         ritual_text = f"✨ **{r['name']}** ✨\n"
#         ritual_text += f"📜 *{r['beschreibung']}*\n\n"

#         for schritt in r['schritte']:
#             ritual_text += f"• {schritt}\n"

#         await interaction.response.send_message(ritual_text)
#     else:
#         keys = ", ".join(rituale.keys())
#         await interaction.response.send_message(
#             f"❌ **Meines kennen dieses Ritual nicht.**\nVerfügbar: `{keys}`",
#             ephemeral=True
#         )

# bot.run(DISCORD_TOKEN)


import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
import random

# Imports deiner Daten aus dem Unterordner 'spirits'
from spirits.wisdom import wisdom
from spirits.visions import visions
from spirits.animals import animals
from spirits.rituals import rituale

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise RuntimeError(
        "Fehler: Bitte setze die Umgebungsvariable DISCORD_TOKEN!")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    # Synchronisiert die Slash-Commands mit Discord
    await bot.tree.sync()
    print(f"Spirit Bot online als {bot.user}")

# --- COMMANDS ---


@bot.tree.command(name="weisheit", description="Die Geister sprechen zu dir.")
async def weisheit(interaction: discord.Interaction):
    text = random.choice(wisdom)
    await interaction.response.send_message(f"🪶 **Die Geister flüstern:**\n{text}")


@bot.tree.command(name="geistertier", description="Ein Geisttier zeigt sich.")
async def geistertier(interaction: discord.Interaction):
    tier, bedeutung = random.choice(list(animals.items()))
    await interaction.response.send_message(f"🐺 **Dein Geisttier ist: {tier}**\nBedeutung: *{bedeutung}*")


@bot.tree.command(name="vision", description="Eine Vision offenbart sich!")
async def vision(interaction: discord.Interaction):
    text = random.choice(visions)
    await interaction.response.send_message(f"🔮 **Vision:**\n{text}")


@bot.tree.command(name="rituals", description="Zeigt die Schritte für ein heiliges Ritual.")
@app_commands.describe(name="Welches Ritual möchtest du durchführen?")
@app_commands.choices(name=[
    app_commands.Choice(name="Reinigungs Ritual", value="reinigung"),
    app_commands.Choice(name="Feuer Ritual", value="feuer"),
    app_commands.Choice(name="Tier Ritual", value="tier"),
    app_commands.Choice(name="Geister Ritual", value="geister"),
    app_commands.Choice(name="Blutmond Ritual", value="blutmond"),
    app_commands.Choice(name="Weltuntergangs Ritual", value="weltuntergang"),
])
async def rituals(interaction: discord.Interaction, name: app_commands.Choice[str]):
    # name.value ist hier der technische Key (z.B. "blutmond")
    r = rituale[name.value]

    ritual_text = f"✨ **{r['name']}** ✨\n"
    ritual_text += f"📜 *{r['beschreibung']}*\n\n"

    for schritt in r['schritte']:
        ritual_text += f"• {schritt}\n"

    await interaction.response.send_message(ritual_text)

# WICHTIG: bot.run IMMER als letzte Zeile!
bot.run(DISCORD_TOKEN)
