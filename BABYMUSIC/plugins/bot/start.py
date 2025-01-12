import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from BABYMUSIC import app
from BABYMUSIC.misc import _boot_
from BABYMUSIC.plugins.sudo.sudoers import sudoers_list
from BABYMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from BABYMUSIC.utils import bot_sys_stats
from BABYMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
    save_user,
    get_user_data,
    update_referrer,
)
from BABYMUSIC.utils.decorators.language import LanguageStart
from BABYMUSIC.utils.formatters import get_readable_time
from BABYMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



YUMI_PICS = [
"https://files.catbox.moe/xhpqtp.jpg",
"https://files.catbox.moe/yeeu8p.jpg",

]

@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        text=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_text(
                    text=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
            

CLONES = """Create your own music bot
Complete 𝐘ᴛ-𝐌ᴜsɪᴄ clone futures
best quality smooth streaming on vc
:- Gᴏ to @BotFather make /newbot 
forward here complete message"""

CHOICE = [
    ["Profile 🪪", "Settings ⚙️"],
    ["Clone 📁", "Refer 📢"],
    ["Language 🌐", "Support 📞"],
]

@app.on_message(filters.private & filters.text & ~BANNED_USERS)
async def clone_handler(client, message):
    if message.text.strip() == "Cʟᴏɴᴇ 📁":
        await message.reply_text(CLONES)
        

@app.on_message(filters.private & filters.text & ~BANNED_USERS)
async def refer_handler(client, message):
    # Check if the message text matches "Rᴇғᴇʀ 📢"
    if message.text.strip() == "Rᴇғᴇʀ 📢":
        user_id = message.from_user.id
        mention = message.from_user.mention

        # Fetch user data from the database
        user_data = await get_user_data(user_id)
        if not user_data:
            await save_user(user_id)
            user_data = await get_user_data(user_id)

        # User points and referral details
        points = user_data.get("points", 0)
        referrals = user_data.get("referrals", 0)

        # Generate referral link
        referral_link = f"https://t.me/{client.me.username}?start={user_id}"
        share_url = f"https://t.me/share/url?url={referral_link}&text=Join%20this%20amazing%20bot%20and%20earn%20points!"

        # Prepare response message
        response = f"""**Hey {mention} 👋**

Here is your referral link. Share and earn points!

1 referral = 20 points 🎉

**Current Points:** {points}
**Total Referrals:** {referrals}

**Your Referral Link:** [Click Here]({referral_link})
"""
        # Send response with a button
        await message.reply_text(
            response,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Share Referral Link", url=share_url)]]
            ),
            disable_web_page_preview=True,
        )

