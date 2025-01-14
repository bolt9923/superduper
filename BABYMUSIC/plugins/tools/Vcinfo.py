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
        user = chat_member_updated.new_chat_member.user  # हो सकता है None हो
        chat_id = chat.id

        # जांचें कि उपयोगकर्ता वॉइस चैट में शामिल हुआ है और दोनों सदस्य None नहीं हैं
        if chat_member_updated.old_chat_member and chat_member_updated.new_chat_member and (
            not chat_member_updated.old_chat_member.is_participant
            and chat_member_updated.new_chat_member.is_participant
        ):
            text = (
                f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                f"Nᴀᴍᴇ: {user.mention}\n"
                f"ɪᴅ: {user.id}\n"
                f"Aᴄᴛɪᴏɴ: Iɢɴᴏʀᴇᴅ"
            )
            await client.send_message(chat_id, text)

    except Exception as e:
        print(f"Error in user_joined_voice_chat: {e}")



# Register the ChatMemberUpdatedHandler
app.add_handler(ChatMemberUpdatedHandler(user_joined_voice_chat))
