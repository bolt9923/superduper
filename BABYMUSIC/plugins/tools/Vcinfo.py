import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.handlers import ChatMemberUpdatedHandler
from pyrogram.types import ChatMemberUpdated
from pyrogram.enums import ChatType
from BABYMUSIC import app


# Handler for notifying when users join voice chats
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        chat = chat_member_updated.chat
        new_chat_member = chat_member_updated.new_chat_member
        user = new_chat_member.user if new_chat_member else None  # Ensure user is not None
        chat_id = chat.id

        # Check if the user joined the voice chat and both members are not None
        if chat_member_updated.old_chat_member and new_chat_member and (
            not chat_member_updated.old_chat_member.is_participant
            and new_chat_member.is_participant
        ):
            if user:  # Only proceed if user is not None
                text = (
                    f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                    f"Nᴀᴍᴇ: {user.mention}\n"
                    f"ɪᴅ: {user.id}\n"
                    f"Aᴄᴛɪᴏɴ: Iɢɴᴏʀᴇᴅ"
                )
                await client.send_message(chat_id, text)
            else:
                print("User is None, skipping message.")

    except Exception as e:
        print(f"Error in user_joined_voice_chat: {e}")




# Register the ChatMemberUpdatedHandler
app.add_handler(ChatMemberUpdatedHandler(user_joined_voice_chat))
