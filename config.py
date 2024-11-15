import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24600747
API_HASH = "bb28ae5ce2b87fa5a6e31e64ba8ea7e2"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7423148448:AAGSv7HRYAZG2H86kl23c4lS_0WhP2l1_KY"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://SirYadav1:YADAV.COM@yadav.vohme.mongodb.net/?retryWrites=true&w=majority&appName=Yadav"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002471042245

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7008504169

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/vpnclouderrrs"
SUPPORT_GROUP = "https://t.me/vpnclouderrrs"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "1BVtsOHYBuwrgIj4LmiMWWr0psWwXlnt7oSkcvjL4r1j_UOWcStNcM-itkEIq9Mjf4nD3Hv9aW1-gJDPFXW5pNGtJeowdsgo8e0ryL6Z40D2J9xArzskb5Btv-8DhXTb-lOCmmAHgKaeffw7KFu5ylMVqat8k5YlFEELD7F6pr9Mu-GDG9JpMKohrDoS3xzuiwmqkV5SSGVZIrV8gOLylt2a4A2xvO-PSikRXCSaB7ocjQFW6ULhadZYiuWc5q-4RUfytkueGuMHzzhnjTNy-lUbXAMCXPac_jRFXe7WRF5_PIS2kn5P2-nLzyKqaW3gHG5z3syCpEGKJDQSnmuj1NOmb_fa6VVI="
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


START_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"

PING_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
STATS_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
STREAM_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/5887669d64d92b2ade09d-56aa77621bd04d2389.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
