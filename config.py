import re
from os import getenv
# ------------------------------------
# ------------------------------------
from dotenv import load_dotenv
from pyrogram import filters
# ------------------------------------
# ------------------------------------
load_dotenv()
# ------------------------------------
# -----------------------------------------------------
API_ID = int(getenv("API_ID", "16457832"))
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")
# ------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7638229482:AAGszFI1I0RidrIf5-FUMCR2GtmuJHTbshQ")
# -------------------------------------------------------
OWNER_USERNAME = getenv("OWNER_USERNAME","untold_coder")
# --------------------------------------------------------
BOT_USERNAME = getenv("BOT_USERNAME" , "leharmusic_bot")
# --------------------------------------------------------
BOT_NAME = getenv("BOT_NAME" , "lehar")
# ---------------------------------------------------------
ASSUSERNAME = getenv("ASSUSERNAME" , "lehar")
# ---------------------------------------------------------


#---------------------------------------------------------------
#---------------------------------------------------------------
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://coder:coder@coder.htbxi.mongodb.net/?retryWrites=true&w=majority")
API_KEY = getenv("API_KEY")
#---------------------------------------------------------------
#---------------------------------------------------------------

# ----------------------------------------------------------------
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
# ----------------------------------------------------------------

# ----------------------------------------------------------------
LOGGER_ID = int(getenv("LOGGER_ID", -1002043570167))
# ----------------------------------------------------------------
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 25))
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 6657539971))
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# config.py
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# ----------------------------------------------------------------
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/BABY-MUSIC/YTM",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/YOUTUBE_RROBOT_UPDATES")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+7jH9qwaLWPsxNWNl")
SOURCE = getenv("SOURCE", "https://github.com/BABY-MUSIC/SPOTIFY_MUSIC")
CHAT = getenv("CHAT", "https://t.me/+7jH9qwaLWPsxNWNl")
# ------------------------------------------------------------------------------
# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
# ----------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# --------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------



# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------
STRING1 = getenv("STRING_SESSION", "BQD7IGgAQZ_o6pSHdyCqBAO2GDmIRxfwvBfNeJPvYC0xJSnwapyZheHg3FEc-kex6gm7wrEiaJxLgYC3zWI5SHsUWvC-TDw3sXBdpOj1QrG4GsKDvLtcsSh86wi5A1ab9rogvqI4o1US_jCT3bebmb4NUWUdP8-8lnefyFhdSVpl8SLr0Gysu7b328SOhMfr3TCooeWKR2KbjcbGRSpTi5LN9qK-81OMrQuHYfBEtTkJo57o9lNRA1_vMdIYjB3b2j9YWiwgIY9tqcNmXLdKNzt8W0OoNZMgfLn3tYJZnlOGbuheDCHfhmjVnUQbEOASxiwizm9uud2r47liD7rsYCK4_WUIFAAAAAHI_A9dAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# ------------------------------------
# ------------------------------------
# ------------------------------------
# ------------------------------------

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/08db892ae10fcd27fc420.jpg"
STATS_IMG_URL = "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/08db892ae10fcd27fc420.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/08db892ae10fcd27fc420.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
# ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
