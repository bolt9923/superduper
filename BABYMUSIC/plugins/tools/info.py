import re
from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import asyncio
from BABYMUSIC.utils.database import clonebotdb  # Replace with the actual module for your database

def escape_markdown(text: str) -> str:
    return re.sub(r'([_\*`\[\]()~>#+-=|{}.!])', r'\\\1', text)

@app.on_message(filters.command('info'))
async def user_info(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Please provide a valid user ID or username.\nUsage: `/info <userid/username>`", quote=True)
        return

    try:
        # Extract user information from the command
        input_data = message.command[1]
        user = await client.get_users(input_data)
        
        # User details
        user_id = user.id
        first_name = escape_markdown(user.first_name or "N/A")
        username = escape_markdown(f"@{user.username}" if user.username else "N/A")
        user_link = f"[Link to Profile](tg://user?id={user_id})"

        # Check user status based on the database
        cloned_bots = clonebotdb.find({"user_id": user_id})  # Query the collection
        cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Convert cursor to list asynchronously

        if cloned_bots_list:
            user_status = "[VIP 💳]"
        else:
            user_status = "[Regular 👥]"

        user_status = escape_markdown(user_status)

        # Send the user's information
        await client.send_message(
            chat_id=message.chat.id,
            text=(
                f"**User Information:**\n"
                f"**ID:** `{user_id}`\n"
                f"**First Name:** `{first_name}`\n"
                f"**Username:** `{username}`\n"
                f"**User Link:** {user_link}\n"
                f"**Status:** `{user_status}`"
            ),
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}\nUnable to fetch user information.", quote=True)
