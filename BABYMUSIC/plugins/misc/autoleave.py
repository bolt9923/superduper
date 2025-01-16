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
            from BABY.core.userbot import assistants

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
                            "No one is listening to song in the voice chat.\n"
                            "Please join voice chat otherwise bot will end song in 15 seconds.",
                        )

                        await asyncio.sleep(15)  # 15 सेकंड का इंतजार करें

                        # फिर से चेक करें कि कोई अन्य सदस्य जुड़ा है या नहीं
                        call_participants = await userbot.get_call_members(chat_id)

                        if len(call_participants) <= 1:  # अगर कोई अन्य सदस्य नहीं है
                            await BABY.stop_stream(chat_id)
                            await app.send_message(
                                chat_id,
                                "No one listed song in voice chat, so the song is ending due to inactivity.",
                            )
                            continue

                except Exception as e:
                    print(f"Error: {e}")
                    pass

                try:
                    await BABY.stop_stream(chat_id)
                except:
                    pass
                try:
                    await app.send_message(
                        chat_id,
                        "No one listed song in voice chat, so the song is ending due to inactivity. 🤒",
                    )
                except:
                    pass


# दोनों फंक्शन्स को असिंक्रोनस रूप से शुरू करें
asyncio.create_task(auto_leave())
asyncio.create_task(auto_end())
