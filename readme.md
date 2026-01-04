🪶 Mini Spirit Bot

Ein kleiner Discord-Bot, der Weisheiten, Visionen und Tierbotschaften teilt.
Dieses Repo ist öffentlich und jeder kann den Bot selbst hosten.

🔹 🔹 🔹 🔹 🔹 🔹 Features 🔹 🔹 🔹 🔹 🔹 🔹 🔹 🔹

/weisheit – zufällige Weisheit aus wisdow.py

/vision – eine Vision aus visions.py

/animals – Informationen aus animals.py

🔧 🔧🔧🔧🔧🔧🔧🔧Voraussetzungen 🔧🔧🔧🔧🔧🔧🔧🔧

Python ≥ 3.11

discord.py (installieren mit):

pip install -r requirements.txt

Eigenen Discord-Bot-Token (aus dem Discord Developer Portal
)

1️⃣ Repo klonen
git clone https://github.com/DEIN_USERNAME/mini_spirit_bot.git
cd mini_spirit_bot

2️⃣ Discord Bot erstellen

Gehe zu Discord Developer Portal

Klicke auf „New Application“ → Name vergeben → erstellen

Gehe zu Bot → Add Bot → Yes

Kopiere den Token (nicht öffentlich teilen!)

3️⃣ Token für den Bot setzen
Option A: Nur für diese Sitzung (einmalig)
$env:DISCORD_TOKEN="DEIN_TOKEN_HIER"
python main.py

Option B: Dauerhaft (Windows)
setx DISCORD_TOKEN "DEIN_TOKEN_HIER"

Terminal neu starten → dann:

python main.py

Option C: .env Datei (einfach, für lokale Tests)

Erstelle im selben Ordner wie main.py eine .env Datei:

DISCORD_TOKEN=DEIN_TOKEN_HIER

Stelle sicher, dass main.py python-dotenv lädt:

from dotenv import load_dotenv
load_dotenv()

Bot starten:

python main.py

4️⃣ Bot auf Discord-Server hinzufügen

Im Developer Portal → OAuth2 → URL Generator

Scopes: bot + applications.commands auswählen

Berechtigungen: Send Messages, Read Message History (evtl. weitere nach Bedarf)

URL generieren → Browser öffnen → Server auswählen → Bot ist drin

5️⃣ Bot starten
python main.py

Ausgabe:

Spirit Bot online als <Botname>

Bot reagiert auf /weisheit, /vision und /animals

⚠️ Hinweise

Token niemals ins Repo einfügen

Jeder Nutzer verwendet seinen eigenen Token

Repo kann öffentlich sein → Bot funktioniert trotzdem

Liste der Texte/Botschaften findest du in spirits/
