import time
import asyncio
import random
import pytz
from datetime import datetime
from pyrogram import filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
from pyrogram.types import KeyboardButton
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
    clonebotdb,
    update_user_data,
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
copy bot token then try
/clone &lt;bot token&gt;

<b><u>NOTE 👇</u></b>
1 bot need 400 points
special vip tag
For 30 days

<u><b>EARN POINTS</b> 🪙</u>
referral link share

<u><b>BUY POINTS</b> 🪙</u>
Do you want directly purchase points
contact:- @UTTAM470"""

SETTING = """ Select settings options
what do you want to know"""

ABOUT = """
🎶 About Music Bot Clone Features 🎧

Our Music Bot Clone comes with advanced features to make your streaming experience even better! 🚀

✨ **Top Features:**
  
🔊 **High-Quality Audio** – Enjoy crystal-clear sound on all tracks.\n
🎥 **Video Streaming** – Supports video as well as audio streaming.\n
⚡ **Fast Response Time** – Instant playback without any lag.\n
🛡️ **No YouTube IP Block** – Stream without any interruptions.\n
🧑‍💻 **Customizable Commands** – Tailor the bot's commands to fit your needs.\n
🎚️ **Adjust Playback Speed** – Control audio speed in both group and channel.\n
💬 **Interactive Features** – Includes user commands like play, pause, skip, volume control, and more.\n
💻 **Supports Multiple Sources** – Works with YouTube, SoundCloud, and other media platforms.\n
📈 **Minimal Downtime** – High uptime with a reliable server structure.\n
🛠️ **Regular Updates** – Stay up-to-date with continuous improvements.

🔒 **Security and Privacy:**
🔑 **Admin Control** – Only admins can modify settings and manage playback.\n
🚫 **Anti-Spam** – Protects groups and channels from spam.\n
👥 **Role-based Access** – Grant different levels of access to users.

🎉 **Join Now and Enjoy Seamless Streaming!**
🌐 More info. Join @BABY09_WORLD 📢
"""

CLONESS = [
    ["Mybots 🤖"],
    ["Back to home 🏠"],
]

SETTINGS = [
    ["About 🖥️", "Help Menu ❗️"],
    ["Back to home 🏠"],
]

CHOICE = [
    ["Profile 🪪", "Settings ⚙️"],
    ["Clone 📁", "Refer 📢"],
    ["Language 🌐", "Support 📞"],
]

@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Clone 📁$"))
async def refer_handler(client, message):
    await message.reply_text(
        text=CLONES,  # Ensure CLONES contains valid text
        reply_markup=ReplyKeyboardMarkup(
            CLONESS,  # This should be a list of button rows
            resize_keyboard=True
        ),
        parse_mode=ParseMode.HTML  # Apply parse_mode here for text formatting
    )

@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^About 🖥️$"))
async def about_handler(client, message):
    await message.reply_text(
        text=ABOUT  # Ensure ABOUT contains valid text
    )

    
@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Settings ⚙️$"))
async def setting_handler(client, message):
    await message.reply_text(
        text=SETTING,  # Ensure CLONES contains valid text
        reply_markup=ReplyKeyboardMarkup(
            SETTINGS,  # This should be a list of button rows
            resize_keyboard=True
        ),
    )

@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Back to home 🏠$"))
async def refer_handler(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention
    
    # Fetch user data from the database
    user_data = await get_user_data(user_id)
    if not user_data:
        await save_user(user_id)
        user_data = await get_user_data(user_id)

    points = user_data.get("points", 0) if user_data else 0
    referrals = user_data.get("referrals", 0) if user_data else 0
    cloned_bots = clonebotdb.find({"user_id": user_id})  # Assuming clonebotdb is the collection for cloned bots

    # Use list() to convert the cursor to a list asynchronously
    cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Run list conversion in a separate thread

    if cloned_bots_list:
        user_status = "[VIP 💳]"
    else:
        user_status = "[Regular 👥]"
    # Generate referral link
    referral_link = f"https://t.me/{client.me.username}?start={user_id}"

    # Prepare response message
    response = f"""**Hey {mention} 👋**
**This is 𝐘ᴛ-𝐌ᴜsɪᴄ**
**The best music|video streaming on VC**

🪙 **Your points:** {points}
📢 **Referrals:** {referrals}
🏷️ **User Tag:** {user_status}

**Your Referral Link:** [Click Here]({referral_link})
"""

    # Send response with user dashboard and buttons
    await message.reply_text(
        text=response,
        reply_markup=ReplyKeyboardMarkup(CHOICE, resize_keyboard=True),
        disable_web_page_preview=True,
    )


@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Profile 🪪$"))
async def profile_handler(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention
    user_data = await get_user_data(user_id)
    points = user_data.get("points", 0) if user_data else 0
    referrals = user_data.get("referrals", 0) if user_data else 0

    # Get current time in Delhi time zone
    delhi_tz = pytz.timezone("Asia/Kolkata")
    delhi_time = datetime.now(delhi_tz)
    current_time = delhi_time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    current_date = delhi_time.strftime("%d-%m-%Y")  # DD-MM-YYYY format

    # Check if the user has cloned any bots to determine their status
    cloned_bots = clonebotdb.find({"user_id": user_id})  # Assuming clonebotdb is the collection for cloned bots

    # Use list() to convert the cursor to a list asynchronously
    cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Run list conversion in a separate thread

    if cloned_bots_list:
        user_status = "[VIP 💳]"
    else:
        user_status = "[Regular 👥]"

    # Build the profile text with the user's status
    profile_text = f"""👤 **Name:** {mention}
🆔 **User ID:** {user_id}

💵 **Balance:** {points} points
💰 **Total Referrals:** {referrals}

💎 **User Tag:** {user_status}

⌚ **Updated On:** {current_time}
📆 **Date:** {current_date}
"""
    await message.reply_text(profile_text)


@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Support 📞$"))
async def refer_handler(client, message):
    await message.reply_text(
        text=SUPPORT,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support 📞", url="https://t.me/+OL6jdTL7JAJjYzVl"),
                    InlineKeyboardButton("Update 🔔", url="https://t.me/BABY09_WORLD")
                ]
            ]
        )
    )


@app.on_message(filters.private & filters.text & ~BANNED_USERS & filters.regex("^Refer 📢$"))
async def refer_handler(client, message):
    # Check if the message text matches "Refer 📢"
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
            return await app.send_message(
                chat_id=user_id,
                text=_["help_1"],
                reply_markup=keyboard,
            )

        elif name == "clone":
            # Create a ReplyKeyboardMarkup
            keyboard = ReplyKeyboardMarkup(
                [[KeyboardButton(text=label[0])] for label in CLONESS],
                resize_keyboard=True,  # Adjust button size
                one_time_keyboard=True  # Hide after one use
            )
            return await client.send_message(
                chat_id=user_id,
                text=CLONES,
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

            # Check if the user has already used the referral link
            user_data = await get_user_data(user_id)
            if user_data and 'referrer' in user_data and user_data['referrer'] == referrer_id:
                # If the referral is already used
                await message.reply_text("This referral link has already been used by you.")
                return

            if referrer and referrer_id != user_id:
                # Save the referral in the database and update referrer points
                await update_referrer(referrer_id)
                await update_user_data(user_id, {"referrer": referrer_id})

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
    cloned_bots = clonebotdb.find({"user_id": user_id})  # Assuming clonebotdb is the collection for cloned bots

    # Use list() to convert the cursor to a list asynchronously
    cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Run list conversion in a separate thread

    if cloned_bots_list:
        user_status = "[VIP 💳]"
    else:
        user_status = "[Regular 👥]"

    # Generate referral link
    referral_link = f"https://t.me/{client.me.username}?start={user_id}"

    # Send user dashboard
    response = f"""**Hey {mention} 👋**
**This is 𝐘ᴛ-𝐌ᴜsɪᴄ**
**The best music|video streaming on VC**

🪙 **Your points:** {points}
📢 **Referrals:** {referrals}
🏷️ **User Tag:** {user_status}

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
async def start_gp(client, message: Message, *args):
    # Create an InlineKeyboardButton with the correct URL
    help_button = InlineKeyboardButton(
        text="Click me for help!",
        url=f"http://t.me/{client.me.username}?start=help"
    )

    # Create an InlineKeyboardMarkup with the button
    reply_markup = InlineKeyboardMarkup([[help_button]])

    # Send the message with the button
    await message.reply_text(
        text="Contact me in PM for help!",
        reply_markup=reply_markup
    )

    # Add the served chat to the database
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    # Get the user who added the bot
    added_by = message.from_user

    for member in message.new_chat_members:
        try:
            buttons = [
                [
                    InlineKeyboardButton("Start in PM", url="http://t.me/Hhfyuhbot?start=start"), 
                    InlineKeyboardButton("Help Menu !", url="http://t.me/Hhfyuhbot?start=help")
                ],
                [InlineKeyboardButton("Get your own bot", url="http://t.me/Hhfyuhbot?start=clone")]
            ]
            reply_markup = InlineKeyboardMarkup(buttons)

            # Check if the new member is the bot itself
            if member.is_self:
                await message.reply_text(
                    text=f"👋 Hey {added_by.mention},\n\n"
                         f"✨ Thank you for adding me to **{message.chat.title}**! I am a **powerful music bot** 🎶 you won't believe. "
                         f"Click the buttons below to explore my features. 🚀",
                    reply_markup=reply_markup
                )
            else:
                await message.reply_text(
                    text=f"👋 Welcome {member.mention}!\n\n"
                         f"✨ Glad to have you in **{message.chat.title}**. Enjoy the music! 🎶",
                    reply_markup=None
                )
        except Exception as ex:
            print(f"Error: {ex}")

