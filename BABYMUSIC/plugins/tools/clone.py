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
from BABYMUSIC.utils.database import get_assistant
from config import API_ID, API_HASH
from BABYMUSIC import app
from BABYMUSIC.misc import SUDOERS
from BABYMUSIC.utils.database import get_assistant, clonebotdb, get_user_data, update_user_points
from config import LOGGER_ID, OWNER_ID

CLONES = set()

@app.on_message(filters.command("addpoint") & filters.user(OWNER_ID))
async def add_points(client, message):
    # Check if the command is in the correct format
    if len(message.command) != 3:
        await message.reply_text("Usage: /addpoint <amount> <user_id>")
        return

    try:
        # Parse the points and user_id from the message
        points_to_add = int(message.command[1])  # Points to add
        user_id = int(message.command[2])  # The user_id to add points to

        # Fetch user data from the database
        user_data = await get_user_data(user_id)
        if not user_data:
            await save_user(user_id)  # Save user if not exists
            user_data = await get_user_data(user_id)

        # Update the user's points in the database
        current_points = user_data.get("points", 0)
        new_points = current_points + points_to_add

        # Update points in the database (this assumes you have a function to update user points)
        await update_user_points(user_id, new_points)

        # Notify the owner that points were added successfully
        await message.reply_text(f"Successfully added {points_to_add} points to user {user_id}. Total points now: {new_points}")

        # Optionally notify the user that their points were updated
        try:
            await client.send_message(
                user_id,
                f"Your points have been updated by the owner! You now have {new_points} points.",
            )
        except Exception as e:
            print(f"Error notifying user: {e}")

    except ValueError:
        await message.reply_text("Invalid format. Please ensure that both the points and user ID are numbers.")


@app.on_message(filters.private & filters.text & filters.regex("^Mybots 🤖$"))
async def my_bots_handler(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention

    # Fetch all cloned bots of the user from the database
    cloned_bots = clonebotdb.find({"user_id": user_id})
    
    # Convert the cursor to a list manually using list()
    cloned_bots_list = await cloned_bots.to_list(length=None)

    if not cloned_bots_list:
        await message.reply_text(f"**Hey {mention} 👋**\n\nYou haven't cloned any bots yet.")
        return

    # Display the cloned bots with clone date and expiry date
    response_text = f"**Your Cloned Bots**:\n\n"
    for bot in cloned_bots_list:
        bot_name = bot["name"]
        bot_username = bot["username"]
        clone_date = bot["clone_date"].strftime("%Y-%m-%d %H:%M:%S")
        expiration_date = bot["expiration_date"].strftime("%Y-%m-%d %H:%M:%S")
        
        response_text += f"""
**Bot Name:** {bot_name}
**Bot Username:** @{bot_username}
**Clone Date:** {clone_date}
**Expiry Date:** {expiration_date}
        """
    
    await message.reply_text(response_text)


@app.on_message(filters.command("clone") & ~BANNED_USERS)
async def clone_txt(client, message):
    user_id = message.from_user.id
    user_data = await get_user_data(user_id)

    # Check if the user has enough points (400 points)
    points = user_data.get("points", 0)
    if points < 400:
        await message.reply_text("❌ You need 400 points to clone a bot.")
        return

    # Deduct 400 points from the user
    new_points = points - 400
    await save_user(user_id, {"points": new_points})  # Update points in the database

    # Process the cloning command
    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        mi = await message.reply_text("Please wait while I process the bot token.")
        try:
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="BABYMUSIC.cplugin"),
            )
            await ai.start()
            bot = await ai.get_me()
            bot_users = await ai.get_users(bot.username)
            bot_id = bot_users.id

        except (AccessTokenExpired, AccessTokenInvalid):
            await mi.edit_text(
                "You have provided an invalid bot token. Please provide a valid bot token."
            )
            return
        except Exception as e:
            await mi.edit_text(f"An error occurred: {str(e)}")
            return

        # Proceed with the cloning process
        await mi.edit_text(
            "Cloning process started. Please wait for the bot to be started."
        )
        try:
            # Save the cloned bot details with an expiration date (30 days from now)
            expiration_date = datetime.now() + timedelta(days=30)

            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": user_id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
                "cloned_by": message.from_user.id,
                "clone_date": datetime.now(),  # Record the cloning date
                "expiration_date": expiration_date,  # Set the expiration date (30 days later)
            }
            clonebotdb.insert_one(details)

            # Log the cloning event
            await app.send_message(
                LOGGER_ID, f"**#New_Clone**\n\n**Bot:- @{bot.username}**"
            )
            await userbot.send_message(bot.username, "/start")

            await mi.edit_text(
                f"Bot @{bot.username} has been successfully cloned and started ✅.\n\n**You will have access to this bot for 30 days.**"
            )

        except Exception as e:
            logging.exception("Error while cloning bot.")
            await mi.edit_text(
                f"⚠️ <b>ᴇʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**ᴋɪɴᴅʟʏ ғᴏᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @vk_zone ᴛᴏ ɢᴇᴛ ᴀssɪsᴛᴀɴᴄᴇ**"
            )

    else:
        await message.reply_text(
            "**Give Bot Token After /clone Command From @Botfather.**"
        )


# Add the function to check the clone expiration periodically

async def check_clone_expiration():
    try:
        # Find all clones and check if they have expired
        now = datetime.now()
        expired_clones = clonebotdb.find({"expiration_date": {"$lt": now}})

        for clone in expired_clones:
            bot_token = clone['token']
            bot_id = clone['bot_id']
            
            # Stop and delete the cloned bot
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="BABYMUSIC.cplugin"),
            )
            await ai.start()

            # Remove the bot from the database
            clonebotdb.delete_one({"bot_id": bot_id})
            
            # Log the removal
            await app.send_message(
                LOGGER_ID, f"**#Clone_Expired**\n\nBot @{clone['username']} has expired and been removed."
            )

            # Stop the bot
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
                "**🤖 your cloned bot has been disconnected from my server ☠️\nClone by :- /clone**"
            )
        else:
            await message.reply_text(
                "**⚠️ The provided bot token is not in the cloned list.**"
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
        cloned_bots = clonebotdb.find()
        cloned_bots_list = await cloned_bots.to_list(length=None)

        if not cloned_bots_list:
            await message.reply_text("No bots have been cloned yet.")
            return

        total_clones = len(cloned_bots_list)
        text = f"Total Cloned Bots: {total_clones}\n\n"

        for bot in cloned_bots_list:
            text += f"Bot ID: {bot['bot_id']}\n"
            text += f"Bot Name: {bot['name']}\n"
            text += f"Bot Username: @{bot['username']}\n\n"

        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("An error occurred while listing cloned bots.")

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(filters.command("delallclone") & SUDOERS)
async def delete_all_clones(client, message):
    if message.from_user.id not in SUDOERS:
        await message.reply_text("❌ You are not authorized to use this command.")
        return
    confirmation_msg = await message.reply_text(
        "⚠️ **Are you sure you want to delete all cloned bots? This action cannot be undone.**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✅ YES", callback_data="confirm_delete"),
                    InlineKeyboardButton("❌ NO", callback_data="cancel_delete"),
                ]
            ]
        ),
    )

    try:
        @app.on_callback_query(filters.user(message.from_user.id))
        async def handle_callback_query(client, callback_query):
            if callback_query.message.id != confirmation_msg.id:
                return

            if callback_query.data == "confirm_delete":
                deleted_count = clonebotdb.delete_many({}).deleted_count
                CLONES.clear()
                await callback_query.message.edit_text(
                    f"✅ Successfully deleted all {deleted_count} cloned bots from the database."
                )
                await client.send_message(
                    LOGGER_ID,
                    f"**#Clones_Deleted**\n\nAll {deleted_count} cloned bots have been deleted by {message.from_user.mention}.",
                )
            elif callback_query.data == "cancel_delete":
                await callback_query.message.edit_text("❌ Action canceled. No bots were deleted.")
            await callback_query.answer()

        await asyncio.sleep(30)
        await confirmation_msg.edit_text("❌ Timeout. No bots were deleted.", reply_markup=None)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("❌ An error occurred while processing your request.")
