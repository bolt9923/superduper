from pyrogram import Client
from pyrogram.types import ChatMemberUpdated
from BABYMUSIC import LOGGER
from BABYMUSIC import app

# Ensure the bot is properly added to the chat and the handler is registered
@app.on_chat_member_updated()
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        # Log the full object to check its structure
        LOGGER.info(f"Chat Member Updated: {chat_member_updated}")

        # Check if the new member is a participant in the voice chat
        if chat_member_updated.new_chat_member.is_participant and not chat_member_updated.old_chat_member.is_participant:
            chat = chat_member_updated.chat
            new_chat_member = chat_member_updated.new_chat_member
            user = new_chat_member.user  # The user who joined
            chat_id = chat.id

            # Log when a user joins the voice chat
            LOGGER.info(f"User {user.id} joined voice chat in chat {chat_id}")

            # Check if the bot has permission to send messages in this chat
            permissions = await client.get_chat_permissions(chat_id, user.id)
            if permissions.can_send_messages:
                text = (
                    f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                    f"Nᴀᴍᴇ: {user.mention}\n"
                    f"ɪᴅ: {user.id}\n"
                    f"Aᴄᴛɪᴏɴ: Jᴏɪɴᴇᴅ"
                )
                await client.send_message(chat_id, text)
                LOGGER.info(f"Message sent to chat {chat_id} for user {user.id}")
            else:
                LOGGER.warning(f"Bot does not have permission to send messages in chat {chat_id}")

        else:
            # Log if the event was triggered but the user didn't actually join
            LOGGER.info("Event triggered, but user didn't join the voice chat.")

    except Exception as e:
        # Log any errors if they occur
        LOGGER.error(f"Error in user_joined_voice_chat: {e}")
