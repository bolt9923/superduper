import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.handlers import ChatMemberUpdatedHandler
from pyrogram.types import ChatMemberUpdated
from pyrogram.enums import ChatType



# Auto Leave Function


# Auto End Function



# Handler for notifying when users join voice chats
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        chat = chat_member_updated.chat
        user = chat_member_updated.new_chat_member.user
        chat_id = chat.id

        if (
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


# Register the ChatMemberUpdatedHandler in Pyrogram
app.on_chat_member_updated(user_joined_voice_chat)
