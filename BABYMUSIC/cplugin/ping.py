import time
from datetime import datetime

import psutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import SUPPORT_CHAT, PING_IMG_URL
from .utils import StartTime
from BABYMUSIC.utils import get_readable_time


@Client.on_message(filters.command("ping"))
async def ping_clone(client: Client, message: Message):
    i = await client.get_me()
    hmm = await message.reply_text(
    text=f"{i.mention} is pinging..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""Pong : `{resp}ms`

<b><u>{i.mention} System stats :</u></b>

🔋 **Uptime :** {uptime}
🧇 **RAM :** {mem}
🔲 **CPU :** {cpu}
💿 **Disk :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support ", url=SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "invite Me",
                        url=f"https://t.me/{i.username}?startgroup=true",
                    ),
                ],
            ]
        ),
    )
