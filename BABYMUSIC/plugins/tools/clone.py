import re
import logging
import asyncio
import importlib
import time
from config import BANNED_USERS
from datetime import datetime, timedelta
from sys import argv
from pyrogram import idle
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import (
    AccessTokenExpired,
    AccessTokenInvalid,
)
from BABYMUSIC.utils.database import get_assistant, save_user
from config import API_ID, API_HASH
from BABYMUSIC import app
from BABYMUSIC.misc import SUDOERS
from BABYMUSIC.utils.database import get_assistant, clonebotdb, get_user_data, update_user_points
from config import LOGGER_ID, OWNER_ID

CLONES = set()

@app.on_message(filters.command("addpoint") & filters.user(OWNER_ID))
async def add_points(client, message):
    if len(message.command) != 3:
        await message.reply_text("Usage: /addpoint <amount> <user_id>")
        return

    try:
        points_to_add = int(message.command[1])  
        user_id = int(message.command[2])  

        user_data = await get_user_data(user_id)
        if not user_data:
            await save_user(user_id)  
            user_data = await get_user_data(user_id)

        current_points = user_data.get("points", 0)
        new_points = current_points + points_to_add

        await update_user_points(user_id, new_points)

        await message.reply_text(f"Successfully added {points_to_add} points to user {user_id}. Total points now: {new_points}")

        try:
            await client.send_message(
                user_id,
                f"Your points have been updated by admin! You now have {new_points} points.",
            )
        except Exception as e:
            print(f"Error notifying user: {e}")

    except ValueError:
        await message.reply_text("Invalid format. Please ensure that both the points and user ID are numbers.")


@app.on_message(filters.private & filters.text & filters.regex("^Mybots 🤖$"))
async def my_bots_handler(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention

    cloned_bots = clonebotdb.find({"user_id": user_id})

    response_text = f"**Your Cloned Bots**:\n\n"
    bot_found = False

    for bot in cloned_bots:
        bot_found = True
        bot_name = bot.get("name", "Unknown")
        bot_username = bot.get("username", "Unknown")
        clone_date = bot.get("clone_date", "Unknown")
        expiration_date = bot.get("expiration_date", "Unknown")

        if isinstance(clone_date, datetime):
            clone_date = clone_date.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(expiration_date, datetime):
            expiration_date = expiration_date.strftime("%Y-%m-%d %H:%M:%S")

        response_text += f"""
**Bot Name:** {bot_name}
**Bot Username:** @{bot_username}
**Clone Date:** {clone_date}
**Expiry Date:** {expiration_date}
        """

    if not bot_found:
        await message.reply_text(f"**Hey {mention} 👋**\n\nYou haven't cloned any bots yet.")
    else:
        await message.reply_text(response_text)


@app.on_message(filters.command("clone"))
async def clone_txt(client, message):
    user_id = message.from_user.id
    userbot = await get_assistant(message.chat.id)

    # Ensure the user provides a bot token
    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        mi = await message.reply_text("Processing the bot token, please wait...")

        # Check user data and points
        user_data = await get_user_data(user_id)
        if not user_data or 'points' not in user_data:
            await mi.edit_text("First start the bot in PM.")
            return

        points = user_data['points']
        if isinstance(points, dict):
            points = points.get("points", 0)

        if points < 400:
            await mi.edit_text("You don't have enough points to clone a bot first earn points 💵")
            return

        try:
            # Initialize bot with the provided token
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="BABYMUSIC.cplugin"),
            )
            await ai.start()
            bot = await ai.get_me()
            bot_username = bot.username
            bot_id = bot.id

        except (AccessTokenExpired, AccessTokenInvalid):
            await mi.edit_text(
                "You have provided an invalid bot token. Please provide a valid bot token."
            )
            return
        except Exception as e:
            await mi.edit_text(f"An error occurred: {str(e)}")
            return

        # Check if the bot is already in the in-memory set
        if bot_id in CLONES:
            await mi.edit_text(
                f"⚠️ Bot @{bot_username} is already running globally.\n\n"
                "If this is your bot, use /delclone to remove it first."
            )
            return

        # Deduct points and proceed with cloning
        new_points = points - 400
        await update_user_points(user_id, new_points)

        try:
            # Save bot details with expiration date
            expiration_date = datetime.now() + timedelta(days=30)
            details = {
                "bot_id": bot_id,
                "is_bot": True,
                "user_id": user_id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot_username,
                "cloned_by": user_id,
                "clone_date": datetime.now(),
                "expiration_date": expiration_date,
            }
            clonebotdb.insert_one(details)
            CLONES.add(bot_id)  # Add bot ID to the in-memory set for tracking

            # Log and notify
            await app.send_message(
                LOGGER_ID, f"**#New_Clone**\n\n**Bot:- @{bot_username}**"
            )
            await userbot.send_message(bot_username, "/start")

            await mi.edit_text(
                f"Bot @{bot_username} has been successfully started ✅.\n\n**For 30 days.**\nRemove any time with /delclone\n\n#SPECIAL_LAUNCH 13 FEBRUARY\nYou can set yourself\n- START_IMG\n- SESSION [assistant]\n- SUPPORT [group]\n- UPDATE [channel]\nNo need to spend more money 🤑\nVisit updates at @YOUTUBE_RROBOT_UPDATES"
            )

        except Exception as e:
            logging.exception("Error while cloning bot.")
            CLONES.discard(bot_id)  # Remove from in-memory set if cloning fails
            await mi.edit_text(
                f"⚠️ <b>Error:</b>\n\n<code>{e}</code>\n\n"
                "**Kindly forward this message to @YTM_Points for assistance.**"
            )
    else:
        await message.reply_text(
            "**Provide the bot token after the /clone command from @Botfather.**"
        )



async def check_clone_expiration():
    try:
        now = datetime.now()
        expired_clones = clonebotdb.find({"expiration_date": {"$lt": now}})

        for clone in expired_clones:
            bot_token = clone['token']
            bot_id = clone['bot_id']
            
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="BABYMUSIC.cplugin"),
            )
            await ai.start()

            clonebotdb.delete_one({"bot_id": bot_id})
            
            await app.send_message(
                LOGGER_ID, f"**#Clone_Expired**\n\nBot @{clone['username']} has expired and been removed."
            )

            await ai.stop()

    except Exception as e:
        logging.exception("Error while checking for expired clones.")



@app.on_message(
    filters.command(
        [
            "deletecloned",
            "delcloned",
            "delclone",
            "deleteclone",
            "removeclone",
            "cancelclone",
        ]
    )
)
async def delete_cloned_bot(client, message):
    try:
        if len(message.command) < 2:
            await message.reply_text(
                "**⚠️ Please provide the bot token after the command.**"
            )
            return

        bot_token = " ".join(message.command[1:])
        await message.reply_text("Processing the bot token...")

        cloned_bot = clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            clonebotdb.delete_one({"token": bot_token})
            CLONES.remove(cloned_bot["bot_id"])
            await message.reply_text(
                "**Your cloned bot has been disconnected from my server ☠️\nClone by :- /clone**"
            )
        else:
            await message.reply_text(
                "**The provided bot token is not in the cloned list.**"
            )
    except Exception as e:
        await message.reply_text("An error occurred while deleting the cloned bot.")
        logging.exception(e)


async def restart_bots():
    global CLONES
    try:
        logging.info("Restarting all cloned bots........")
        bots = clonebotdb.find()
        for bot in bots:
            bot_token = bot["token"]
            ai = Client(
                f"{bot_token}",
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="BABYMUSIC.cplugin"),
            )
            await ai.start()
            bot = await ai.get_me()
            if bot.id not in CLONES:
                try:
                    CLONES.add(bot.id)
                except Exception:
                    pass
    except Exception as e:
        logging.exception("Error while restarting bots.")


@app.on_message(filters.command("cloned") & SUDOERS)
async def list_cloned_bots(client, message):
    try:
        cloned_bots = clonebotdb.find()  # Assuming clonebotdb is a synchronous MongoDB collection
        cloned_bots_list = list(cloned_bots)  # Use list() to convert the cursor

        if not cloned_bots_list:
            await message.reply_text("No bots have been cloned yet.")
            return

        total_clones = len(cloned_bots_list)
        text = f"Total Cloned Bots: {total_clones}\n\n"

        for bot in cloned_bots_list:
            text += f"Bot ID: {bot['bot_id']}\n"
            text += f"Bot Name: {bot['name']}\n"
            text += f"Bot Username: @{bot['username']}\n"
            text += f"Bot Token: `{bot['token']}`\n\n"  # Adding Bot Token

        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("An error occurred while listing cloned bots.")


@app.on_message(filters.command("delallclone") & SUDOERS)
async def delete_all_clones(client, message):
    if message.from_user.id not in SUDOERS:
        return
    
    try:
        cloned_bots = clonebotdb.find({})

        deleted_count = 0
        for bot in cloned_bots:
            bot_token = bot["token"]
            try:
                ai = Client(
                    bot_token,
                    API_ID,
                    API_HASH,
                    bot_token=bot_token,
                    plugins=dict(root="BABYMUSIC.cplugin"),
                )
                await ai.start()
                await ai.stop()  
                deleted_count += 1  
            except Exception as e:
                logging.error(f"Error stopping bot with token {bot_token}: {e}")

        deleted_count += clonebotdb.delete_many({}).deleted_count
        
        CLONES.clear()  

        await message.reply_text(
            f"✅ Successfully deleted and stopped all {deleted_count} cloned bots."
        )

        await client.send_message(
            LOGGER_ID,
            f"**#Clones_Deleted_And_Stopped**\n\nAll {deleted_count} cloned bots have been deleted and stopped by {message.from_user.mention}.",
        )

    except Exception as e:
        logging.exception("Error deleting and stopping clones.")
        await message.reply_text("❌ An error occurred while deleting and stopping cloned bots.")
