import re
from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import Message
import asyncio
from BABYMUSIC.utils.database import clonebotdb # Replace with the actual module for your database

# Define a default image URL or file ID
DEFAULT_IMG = 'https://files.catbox.moe/01i7ch.jpg'  # Replace with the actual URL or file ID



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
        first_name = user.first_name or "N/A"
        username = f"@{user.username}" if user.username else "N/A"
        user_link = f"[Link to Profile](tg://user?id={user_id})"

        # Check user status based on the database
        cloned_bots = clonebotdb.find({"user_id": user_id})  # Query the collection
        cloned_bots_list = await asyncio.to_thread(list, cloned_bots)  # Convert cursor to list asynchronously

        if cloned_bots_list:
            user_status = "[VIP 💳]"
        else:
            user_status = "[Regular 👥]"

        # Escape special characters for Markdown compatibility
        user_status = escape_markdown(user_status)
        first_name = escape_markdown(first_name)
        username = escape_markdown(username)
        user_link = escape_markdown(user_link)

        # User photo (using `client.get_profile_photos` to fetch the user's profile photo)
        profile_photos = await client.get_profile_photos(user.id)
        if profile_photos.total_count > 0:
            # If the user has a profile photo, use it
            photo = profile_photos.photos[0].file_id
        else:
            # Use the default image if no profile photo exists
            photo = DEFAULT_IMG

        # Send the user's information
        await client.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=(
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
