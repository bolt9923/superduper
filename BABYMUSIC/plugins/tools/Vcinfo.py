from pyrogram import Client
from pyrogram.types import ChatMemberUpdated
from BABYMUSIC import LOGGER
from BABYMUSIC import app

# Handler function
# Handler function
@app.on_chat_member_updated()
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        # Log the entire chat_member_updated for debugging
        LOGGER.info(f"Chat Member Updated: {chat_member_updated}")

        # Check if the user has joined the voice chat (is_participant=True)
        if chat_member_updated.new_chat_member.is_participant and not chat_member_updated.old_chat_member.is_participant:
            chat = chat_member_updated.chat
            new_chat_member = chat_member_updated.new_chat_member
            user = new_chat_member.user  # The user who joined
            chat_id = chat.id

            # Log user and chat details
            LOGGER.info(f"User {user.id} joined voice chat in chat {chat_id}")

            # Send a message in the chat if user joined the voice chat
            text = (
                f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                f"Nᴀᴍᴇ: {user.mention}\n"
                f"ɪᴅ: {user.id}\n"
                f"Aᴄᴛɪᴏɴ: Jᴏɪɴᴇᴅ"
            )
            await client.send_message(chat_id, text)
        else:
            # If the event was triggered, but the user didn't actually join, log it
            LOGGER.info("Event triggered, but user didn't join the voice chat.")

    except Exception as e:
        # Log the error if it occurs
        LOGGER.error(f"Error in user_joined_voice_chat: {e}")
