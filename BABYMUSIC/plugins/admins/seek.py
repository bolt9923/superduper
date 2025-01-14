from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
import math
from BABYMUSIC import YouTube, app
from BABYMUSIC.core.call import BABY
from BABYMUSIC.misc import db
from BABYMUSIC.utils import AdminRightsCheck, seconds_to_min
from BABYMUSIC.utils.inline import close_markup
from config import BANNED_USERS


# Command handler for seeking
@app.on_message(
    filters.command(["seek", "cseek", "seekback", "cseekback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def seek_comm(cli, message: Message, _, chat_id):
    if len(message.command) == 1:
        return await message.reply_text(_["admin_20"])
    query = message.text.split(None, 1)[1].strip()
    if not query.isnumeric():
        return await message.reply_text(_["admin_21"])
    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await message.reply_text(_["admin_22"])
    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])
    duration_to_skip = int(query)
    duration = playing[0]["dur"]
    if message.command[0][-2] == "c":
        if (duration_played - duration_to_skip) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played - duration_to_skip + 1
    else:
        if (duration_seconds - (duration_played + duration_to_skip)) <= 10:
            return await message.reply_text(
                text=_["admin_23"].format(seconds_to_min(duration_played), duration),
                reply_markup=close_markup(_),
            )
        to_seek = duration_played + duration_to_skip + 1
    mystic = await message.reply_text(_["admin_24"])
    if "vid_" in file_path:
        n, file_path = await YouTube.video(playing[0]["vidid"], True)
        if n == 0:
            return await message.reply_text(_["admin_22"])
    check = (playing[0]).get("speed_path")
    if check:
        file_path = check
    if "index_" in file_path:
        file_path = playing[0]["vidid"]
    try:
        await BABY.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(to_seek),
            duration,
            playing[0]["streamtype"],
        )
    except:
        return await mystic.edit_text(_["admin_26"], reply_markup=close_markup(_))
    if message.command[0][-2] == "c":
        db[chat_id][0]["played"] -= duration_to_skip
    else:
        db[chat_id][0]["played"] += duration_to_skip
    await mystic.edit_text(
        text=_["admin_25"].format(seconds_to_min(to_seek), message.from_user.mention),
        reply_markup=close_markup(_),
    )


# Callback handler for seek buttons
@app.on_callback_query(filters.regex("SEEK"))
async def seek_callback(cli, query: CallbackQuery):
    data = query.data.split("|")
    action = data[0]  # SEEKBACKWARD or SEEKFORWARD
    chat_id = int(data[1])
    seconds = int(data[2])

    playing = db.get(chat_id)
    if not playing:
        return await query.answer("No music is playing in this chat!", show_alert=True)

    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await query.answer("This stream doesn't support seeking!", show_alert=True)

    file_path = playing[0]["file"]
    duration_played = int(playing[0]["played"])

    if action == "SEEKBACKWARD":
        new_position = duration_played - seconds
        if new_position <= 0:
            return await query.answer("Cannot seek beyond the start of the stream!", show_alert=True)
    elif action == "SEEKFORWARD":
        new_position = duration_played + seconds
        if (duration_seconds - new_position) <= 10:
            return await query.answer("Cannot seek beyond the end of the stream!", show_alert=True)
    else:
        return await query.answer("Invalid action!", show_alert=True)

    # Send seek command to the player
    try:
        if "vid_" in file_path:
            n, file_path = await YouTube.video(playing[0]["vidid"], True)
            if n == 0:
                return await query.answer("Failed to fetch the video!", show_alert=True)
        check = (playing[0]).get("speed_path")
        if check:
            file_path = check
        if "index_" in file_path:
            file_path = playing[0]["vidid"]

        await BABY.seek_stream(
            chat_id,
            file_path,
            seconds_to_min(new_position),
            seconds_to_min(duration_seconds),
            playing[0]["streamtype"],
        )
    except Exception as e:
        return await query.answer("Failed to seek stream!", show_alert=True)

    # Update the database with the new playback position
    db[chat_id][0]["played"] = new_position

    await query.answer(
        f"Moved to {seconds_to_min(new_position)}.",
        show_alert=True
    )

