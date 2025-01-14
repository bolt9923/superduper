from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import asyncio
from BABYMUSIC.utils.database import clonebotdb  # Replace with the actual module for your database

@app.on_message(filters.command('info'))
async def user_info(client: Client, message: Message):
    try:
        # Check if user has provided an argument
        if len(message.command) < 2:
            # Send a guide if no argument is provided
            await message.reply_text(
                "**Usage Guide:**\n"
                "`/info <userid/username>`\n\n"
                "**Examples:**\n"
                "`/info 123456789`\n"
                "`/info @username`\n\n"
                "Please provide a valid user ID or username to get their information.",
                parse_mode=ParseMode.MARKDOWN,
                reply_to_message_id=message.id,
            )
            return

        # Extract user information from the command
        input_data = message.command[1]
        user = await client.get_users(input_data)
        
        # User details
        user_id = user.id
        first_name = user.first_name or "N/A"
        username = f"@{user.username}" if user.username else "N/A"
        user_link = f"[link](tg://user?id={user_id})"

        # Check user status based on the database
        cloned_bots = clonebotdb.find({"user_id": user_id})  # Query the collection
        cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Convert cursor to list asynchronously

        if cloned_bots_list:
            user_status = "[VIP 💳]"
        else:
            user_status = "[Regular 👥]"

        # Send the user's information
        await client.send_message(
            chat_id=message.chat.id,
            text=(
                f"**User Information:**\n"
                f"**ID:** `{user_id}`\n"
                f"**First Name:** `{first_name}`\n"
                f"**Username:** {username}\n"
                f"**User Link:** {user_link}\n"
                f"**Status:** {user_status}"
            ),
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}\nUnable to fetch user information.", quote=True)
