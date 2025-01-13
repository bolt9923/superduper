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
            from SONALI.core.userbot import assistants

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




# सभी चैट्स के लिए वॉयस चैट पार्टिसिपेंट्स को ट्रैक करने के लिए एक डिक्शनरी
vc_participants = {}

async def auto_end():
    while not await asyncio.sleep(5):  # हर 5 सेकंड में चेक करता है
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
                    current_participants = await userbot.get_call_members(chat_id)

                    # पुरानी लिस्ट से तुलना करें और नए यूजर्स को डिटेक्ट करें
                    previous_participants = vc_participants.get(chat_id, set())
                    current_ids = {user.peer_id.user_id for user in current_participants}

                    new_users = current_ids - previous_participants

                    # नए यूजर्स के लिए मैसेज भेजें
                    for user_id in new_users:
                        try:
                            user = await app.get_users(user_id)
                            await app.send_message(
                                chat_id,
                                f"{user.first_name} joined the voice chat."
                            )
                        except Exception as e:
                            print(f"Error fetching user info: {e}")

                    # वॉयस चैट में केवल बॉट होने पर वार्निंग मैसेज भेजें
                    if len(current_participants) <= 1:  # अगर सिर्फ बॉट है
                        await app.send_message(
                            chat_id,
                            "No one is listening to song in the voice chat.\n"
                            "Please join the voice chat otherwise bot will end song in 15 seconds.",
                        )

                        await asyncio.sleep(15)  # 15 सेकंड का इंतजार करें

                        # फिर से चेक करें कि कोई अन्य सदस्य जुड़ा है या नहीं
                        current_participants = await userbot.get_call_members(chat_id)

                        if len(current_participants) <= 1:  # अगर कोई अन्य सदस्य नहीं है
                            await RAUSHAN.stop_stream(chat_id)
                            await app.send_message(
                                chat_id,
                                "No one joined the voice chat, the song is ending due to inactivity.",
                            )
                            continue

                    # नई लिस्ट को अपडेट करें
                    vc_participants[chat_id] = current_ids

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
                        "Assistant stopped the song and left the voice chat due to no one listening.",
                    )
                except:
                    pass

