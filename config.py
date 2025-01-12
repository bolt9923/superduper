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
BOT_TOKEN = getenv("BOT_TOKEN", "7532369778:AAGlE49WwuHcCsPYxPEWC87GmuzikO2Ekg8")
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
# ----------------------------------------------------------------
OWNER_ID = int(getenv("OWNER_ID", 7400383704))
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
    "https://github.com/MOON-CODES/Clonesss",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # ----------------------------------------------------------------
# -------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------



# ------------------------------------------------------------------------
# -------------------------------------------------------------------------
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/untold_coder")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/world_friend_chatting_zone")
SOURCE = getenv("SOURCE", "https://t.me/Moon_Music_Updates")
CHAT = getenv("CHAT", "https://t.me/world_friend_chatting_zone")
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
STRING1 = getenv("STRING_SESSION", "BQD7IGgAfzHCVAkQ_b8OFmQWfmfb52MbWIJdDpQyGq7XYzKpQv67E4KRGquvRmi2OW27xzPelXI0YnBSqmz8n7HODEtN62zSWBJjtdqBXRyYESAjEAQIEc16EvMdDls1_OHvlNcCkrUFc_xsr68DjGU7XiBnCCPglfR_FERbM6ybJMIgQj028IHJMHl9HrtFxOjG-ywYol9SQC66-Bfq_HwFbJ2pDMNQc2R4Y8csmvFmaQcdKuw1_JP8gQ2n9BrO-uWHt6IYFS43T4IAcq9FmiBLVocpXH9Rv1-ZW5xArsCIQzOfMC39Tv9eMJzwKE2P7sLGYoPhX0oCzVHN3A7Br0tjRA5QNwAAAAGvPSEfAA")
STRING2 = getenv("STRING_SESSION2", None)
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
