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

SUPPORT = """👉🏻 Send me any message with a request to support.

💡 The send message like discussion, facing issues, other message sender [spam, time waste] ban.

⚠️ We do NOT provide support for ban, mute or other things related to this bot: for this kind of requests contact the group administrators directly.

💡 Visit support chat"""

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

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    user_id = message.from_user.id
    mention = message.from_user.mention

    # Handle if the message contains extra text
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1].lower()

        # Handle the 'help' command
        if name.startswith("help"):
            keyboard = help_pannel(_)
            return await message.send_message(
                text=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )

        # Handle the 'sud' command
        elif name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"✦ {mention} just started the bot to check <b>sudolist</b>.\n\n<b>✦ User ID ➠</b> <code>{user_id}</code>\n<b>✦ Username ➠</b> @{message.from_user.username}",
                )
            return

        # Handle the 'inf' command
        elif name.startswith("inf"):
            m = await message.reply_text("🔎")
            query = name.replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)

            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]

            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )

            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"✦ {mention} just started the bot to check <b>track information</b>.\n\n✦ <b>User ID ➠</b> <code>{user_id}</code>\n✦ <b>Username ➠</b> @{message.from_user.username}",
                )

        # Handle referral logic
        elif name.isdigit():
            referrer_id = int(name)
            referrer = await get_user_data(referrer_id)
            if referrer and referrer_id != user_id:
                await update_referrer(referrer_id)
                # Send message to the referrer
                await app.send_message(
                    referrer_id,
                    text=f"🎉 New user {mention} joined using your referral link!",
                )

    # Check if the user already exists in the database
    user_data = await get_user_data(user_id)
    if not user_data:
        await save_user(user_id)
        user_data = await get_user_data(user_id)

    # Fetch user data
    points = user_data.get("points", 0)
    referrals = user_data.get("referrals", 0)

    # Generate referral link
    referral_link = f"https://t.me/{client.me.username}?start={user_id}"

    # Send user dashboard
    response = f"""**Hey {mention} 👋**
**This is 𝐘ᴛ-𝐌ᴜsɪᴄ**
**The best music|video streaming on VC**

**Your points:** {points}
**Referrals:** {referrals}
**User:** [regular]

**Your Referral Link:** [Click Here]({referral_link})"""

    await message.reply_text(
        text=response,
        reply_markup=ReplyKeyboardMarkup(CHOICE, resize_keyboard=True),
        disable_web_page_preview=True,
    )

    # Log the start event if enabled
    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOGGER_ID,
            text=f"✦ {mention} just started the bot.\n\n✦ <b>User ID ➠</b> <code>{user_id}</code>\n✦ <b>Username ➠</b> @{message.from_user.username}",
        )
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
            

