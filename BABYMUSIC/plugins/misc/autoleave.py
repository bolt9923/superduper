import asyncio
from datetime import datetime

from pyrogram.enums import ChatType
import config
from BABYMUSIC import app
from BABYMUSIC.core.call import BABY, autoend
from BABYMUSIC.utils.database import get_client, is_active_chat, is_autoend


# ऑटो लीव फंक्शन
async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while not await asyncio.sleep(900):  # हर 15 मिनट में चेक करता रहेगा
            from BABYMUSIC.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001465277194
                                and i.chat.id != -1002120144597
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


# ऑटो एंड फंक्शन
async def auto_end():
    while not await asyncio.sleep(5):  # हर 5 सेकंड में चेक करता है
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue

                autoend[chat_id] = {}
                try:
                    # वॉयस चैट के पार्टिसिपेंट्स चेक करें
                    userbot = await get_client(chat_id)
                    call_participants = await userbot.get_call_members(chat_id)

                    if len(call_participants) <= 1:  # अगर सिर्फ बॉट है
                        await app.send_message(
                            chat_id,
                            "❍ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ ᴛᴏ sᴏɴɢ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n"
                            "ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏᴛʜᴇʀᴡɪsᴇ ʙᴏᴛ ᴡɪʟʟ ᴇɴᴅ sᴏɴɢ ɪɴ 15 sᴇᴄᴏɴᴅs.",
                        )

                        await asyncio.sleep(15)  # 15 सेकंड का इंतजार करें

                        # फिर से चेक करें कि कोई अन्य सदस्य जुड़ा है या नहीं
                        call_participants = await userbot.get_call_members(chat_id)

                        if len(call_participants) <= 1:  # अगर कोई अन्य सदस्य नहीं है
                            await RAUSHAN.stop_stream(chat_id)
                            await app.send_message(
                                chat_id,
                                "❍ ɴᴏ ᴏɴᴇ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ, sᴏ ᴛʜᴇ sᴏɴɢ ɪs ᴇɴᴅɪɴɢ ᴅᴜᴇ ᴛᴏ ɪɴᴀᴄᴛɪᴠɪᴛʏ.",
                            )
                            continue

                except Exception as e:
                    print(f"Error: {e}")
                    pass

                try:
                    await RAUSHAN.stop_stream(chat_id)
                except:
                    pass
                try:
                    await app.send_message(
                        chat_id,
                        "𝐎ʜʜ 𝐍ᴏ 𝐒ᴏɴɢ 𝐄ɴᴅ 𝐊ᴏɪ 𝐍ᴀ 𝐌ᴀɪ 𝐉ᴀ 𝐑ᴀʜɪ 𝐇ᴜ😐 𝐀ᴀᴛɪ 𝐇ᴜ 𝐅ɪʀ🤭",
                    )
                except:
                    pass


from pyrogram import Client, filters
from pyrogram.handlers import ChatMemberUpdatedHandler
from pyrogram.types import ChatMemberUpdated, Message
from typing import Union, List

# Default state for /infovc
infovc_enabled = True  # Default to always true

# Command decorator
def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")

# Command to toggle /infovc on/off
@app.on_message(command(["infovc"]))
async def toggle_infovc(_, message: Message):
    global infovc_enabled
    if len(message.command) > 1:
        state = message.command[1].lower()
        if state == "on":
            infovc_enabled = True
            await message.reply("✅ Voice chat join notifications are now enabled.")
        elif state == "off":
            infovc_enabled = False
            await message.reply("❌ Voice chat join notifications are now disabled.")
        else:
            await message.reply("⚠️ Usage: /infovc on or /infovc off")
    else:
        await message.reply("⚠️ Usage: /infovc on or /infovc off")

# Handler to notify when users join voice chats
async def user_joined_voice_chat(client: Client, chat_member_updated: ChatMemberUpdated):
    global infovc_enabled

    try:
        # Check if notifications are enabled
        if not infovc_enabled:
            return

        chat = chat_member_updated.chat
        user = chat_member_updated.new_chat_member.user
        chat_id = chat.id

        # Debug: Print event details
        print(f"ChatMemberUpdated event: {chat_member_updated}")

        # Check if the event is related to joining a voice chat
        if (
            not chat_member_updated.old_chat_member.is_participant
            and chat_member_updated.new_chat_member.is_participant
        ):
            # Construct the message
            text = (
                f"#JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                f"Nᴀᴍᴇ: {user.mention}\n"
                f"ɪᴅ: {user.id}\n"
                f"Aᴄᴛɪᴏɴ: Iɢɴᴏʀᴇᴅ"
            )

            # Debug: Print the message before sending
            print(f"Message to send: {text}")

            # Send the message
            await client.send_message(chat_id, text)
    except Exception as e:
        # Log any errors
        print(f"Error in user_joined_voice_chat: {e}")

# Register the ChatMemberUpdatedHandler
app.add_handler(ChatMemberUpdatedHandler(user_joined_voice_chat))
# दोनों फंक्शन्स को असिंक्रोनस रूप से शुरू करें
asyncio.create_task(auto_leave())
asyncio.create_task(auto_end())
