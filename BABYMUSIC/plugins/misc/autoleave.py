import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.handlers import ChatMemberUpdatedHandler
from pyrogram.types import ChatMemberUpdated, Message
from pyrogram.enums import ChatType
from typing import Union, List

import config
from BABYMUSIC import app
from BABYMUSIC.core.call import BABY, autoend
from BABYMUSIC.utils.database import get_client, is_active_chat, is_autoend


# Auto Leave Function
async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while True:
            await asyncio.sleep(900)  # Every 15 minutes
            from BABYMUSIC.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for dialog in client.get_dialogs():
                        if dialog.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP, ChatType.CHANNEL]:
                            if (
                                dialog.chat.id != config.LOGGER_ID
                                and dialog.chat.id != -1001465277194
                                and dialog.chat.id != -1002120144597
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(dialog.chat.id):
                                    try:
                                        await client.leave_chat(dialog.chat.id)
                                        left += 1
                                    except Exception:
                                        continue
                except Exception:
                    pass

# Auto End Function
async def auto_end():
    while True:
        await asyncio.sleep(5)  # Every 5 seconds
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
                    userbot = await get_client(chat_id)
                    call_participants = await userbot.get_call_members(chat_id)

                    if len(call_participants) <= 1:  # Only bot is present
                        await app.send_message(
                            chat_id,
                            "❍ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ ᴛᴏ sᴏɴɢ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n"
                            "ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏᴛʜᴇʀᴡɪsᴇ ʙᴏᴛ ᴡɪʟʟ ᴇɴᴅ sᴏɴɢ ɪɴ 15 sᴇᴄᴏɴᴅs.",
                        )
                        await asyncio.sleep(15)
                        call_participants = await userbot.get_call_members(chat_id)
                        if len(call_participants) <= 1:  # No new participants
                            await BABY.stop_stream(chat_id)
                            await app.send_message(
                                chat_id,
                                "❍ ɴᴏ ᴏɴᴇ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ, sᴏ ᴛʜᴇ sᴏɴɢ ɪs ᴇɴᴅɪɴɢ ᴅᴜᴇ ᴛᴏ ɪɴᴀᴄᴛɪᴠɪᴛʏ.",
                            )
                            continue
                except Exception as e:
                    print(f"Error: {e}")
                    pass

                try:
                    await BABY.stop_stream(chat_id)
                except Exception:
                    pass

# Schedule tasks
loop = asyncio.get_event_loop()
loop.create_task(auto_leave())
loop.create_task(auto_end())
