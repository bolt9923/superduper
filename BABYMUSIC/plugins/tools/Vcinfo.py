from pyrogram import Client
from pyrogram.handlers import ChatMemberUpdatedHandler
from pyrogram.types import ChatMemberUpdated
from BABYMUSIC import LOGGER, app

# Handler function to check if user joined voice chat
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        # Log the full chat_member_updated for debugging
        LOGGER.info(f"Chat Member Updated: {chat_member_updated}")

        # Check if the new member is a participant in the voice chat
        if chat_member_updated.new_chat_member.is_participant and not chat_member_updated.old_chat_member.is_participant:
            chat = chat_member_updated.chat
            new_chat_member = chat_member_updated.new_chat_member
            user = new_chat_member.user  # The user who joined
            chat_id = chat.id

            # Log when a user joins the voice chat
            LOGGER.info(f"User {user.id} joined voice chat in chat {chat_id}")

            # Send a message to the chat
            text = (
                f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                f"Nᴀᴍᴇ: {user.mention}\n"
                f"ɪᴅ: {user.id}\n"
                f"Aᴄᴛɪᴏɴ: Jᴏɪɴᴇᴅ"
            )
            await client.send_message(chat_id, text)
            LOGGER.info(f"Message sent to chat {chat_id} for user {user.id}")
        else:
            # Log if the event was triggered but the user didn't actually join the voice chat
            LOGGER.info("Event triggered, but user didn't join the voice chat.")

    except Exception as e:
        # Log the error if it occurs
        LOGGER.error(f"Error in user_joined_voice_chat: {e}")

# Register the handler before app.run()
app.add_handler(ChatMemberUpdatedHandler(user_joined_voice_chat))

# Run the app without the 'use_qr' argument
app.run()
