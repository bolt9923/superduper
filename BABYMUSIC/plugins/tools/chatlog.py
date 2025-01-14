import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID
from BABYMUSIC import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://files.catbox.moe/xnmc4b.jpg",
    "https://files.catbox.moe/o17hgj.jpg",
    "https://files.catbox.moe/tolvrn.jpg",
    "https://files.catbox.moe/wsuo4n.jpg",
    "https://files.catbox.moe/o17hgj.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"#Music_added_in_a_new_group 🎉n\n"
                f"____________________________________\n\n"
                f"💬 Chat name: {chat.title}\n"
                f"🆔 Chat ID: {chat.id}\n"
                f"🦋 Chat username: @{chat.username}\n"
                f"🔗 Chat link: [click]({link})\n"
                f"👥 Group members: {count}\n"
                f"🙋🏻‍♂️ Added By: {message.from_user.mention}"
            )
            await app.send_photo(LOGGER_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Group link 🔗", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"<b><u>#Music_bot_leave 🤖</u></b>\n\n💬 Chat title : {title}\n\n🆔 Chat ID : {chat_id}\n\n🙍🏻‍♂️ Removed by : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOGGER_ID, photo=random.choice(photo), caption=left)
        
