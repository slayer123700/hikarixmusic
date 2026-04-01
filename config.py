import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# --- API CREDENTIALS ---
# Get these from my.telegram.org
API_ID = int(getenv("API_ID", 22657083))
API_HASH = getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")

# Get your token from @BotFather
BOT_TOKEN = getenv("BOT_TOKEN", "8752427731:AAFWD6FLAVe8YIGtjuTPZNEaEgRMufUnoWY")

# --- DATABASE ---
# This was the cause of your crash. Fixed to use your Atlas URL as default.
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://maxx99596_db_user:zXx9k0yY9ruCvNJV@cluster0.aamlvxf.mongodb.net/?appName=Cluster0")

# --- LOGGING & OWNER ---
LOGGER_ID = int(getenv("LOGGER_ID", -1003824737197))
OWNER_ID = int(getenv("OWNER_ID", 5303251380))
START_STICKER_FILE_ID = [
         "CAACAgUAAyEFAASjn0HcAAIrtWl5_yUhw2hw2JxcLyCiD0ozBk16AAKOEwACU7ygVbR1uQXoKUAWHgQ",
         "CAACAgUAAyEFAASjn0HcAAIrtGl5_x3YBGxKoRLNoFNtmYHZsSZLAAJGEwACfT2ZVUzSXwryvD51HgQ",
    ]

# --- LIMITS & MODES ---
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))
ADS_MODE = getenv("ADS_MODE", None)
DEBUG_IGNORE_LOG = True
BOT_VERSION = "𝑆𝑙𝑎𝑦𝑒𝑟2.𝑂"

# --- HEROKU CONFIGURATION ---
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "hikari")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-AArEwk2VzkV34TPhdvIMNUvVNUqOORRE2rKwVwZC0nqw_____wa5cyLZDJm9")

# --- REPO & SUPPORT ---
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RolexXd/hikarixmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None) 

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/OnyxCoders")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LavenderEchoo")

# --- ASSISTANT SETTINGS ---
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
STRING1 = getenv("STRING_SESSION", "BQFZuDsAouZN1R-YTyJuYLcxPXe5xVqRpUbeX3BbZOZO3BWA71cP2eRG1ObwpTOcT1Onf0rageIj63zLLHtrkHLQgCTAk7_SWhnK1poutTuR9xUBVH1RDObr1R_hZ6K6KKrJOw0reEnPOP3fnMl4nJW0rZH9gpDhi0ujolVisBDnyObPKeiYUDum1-qDa46VJf3gvlFpjUI2cj-PyIOvXTmF1DuAIhjTdIJsKupGR2rhrj4_r6q7Yx8PSxvXsEvxamMQ02FYBb1qSYRr-y00mNTQellRe18HL8osEzI_kMnnVPRoypXOrmVFcn1du3oEGdsrVRYDwwTfelDdpLjerkZbKa-JVQAAAAIFh15BAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# --- EXTERNAL SERVICES ---
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# --- FILE LIMITS ---
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# --- GLOBALS ---
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# --- IMAGES ---
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/34xlvu.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/34xlvu.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
STATS_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/d6d42f.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/d6d42f.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/d6d42f.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/34xlvu.jpg"

# --- HELPER FUNCTIONS ---
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# --- VALIDATION ---
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong.")

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong.")
