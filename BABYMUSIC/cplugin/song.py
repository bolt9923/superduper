import os
import requests
import yt_dlp
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from config import SUPPORT_CHAT


def time_to_seconds(time):
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(":"))))


@Client.on_message(filters.command(["song", "music"]))
async def song(client, message):
    try:
        await message.delete()

        if len(message.command) < 2:
            return await message.reply_text("**Please specify a song name to search.**")

        user_id = message.from_user.id
        user_name = message.from_user.first_name
        requester = f"[{user_name}](tg://user?id={user_id})"

        query = " ".join(message.command[1:])
        print(f"Searching for: {query}")

        progress_msg = await message.reply("**Searching...**")

        ydl_opts = {"format": "bestaudio[ext=m4a]"}

        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            video_data = results[0]
            link = f"https://youtube.com{video_data['url_suffix']}"
            title = video_data["title"][:40]
            thumbnail_url = video_data["thumbnails"][0]
            duration = video_data["duration"]
            views = video_data["views"]

            # Download thumbnail
            thumb_name = f"thumb_{title}.jpg"
            thumb_data = requests.get(thumbnail_url, allow_redirects=True).content
            with open(thumb_name, "wb") as thumb_file:
                thumb_file.write(thumb_data)

        except Exception as e:
            await progress_msg.edit("**Song not found.**\n\nTry another song!")
            print(f"Error fetching song: {e}")
            return

        await progress_msg.edit("**Downloading...**\n\nPlease wait...")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=False)
                audio_file = ydl.prepare_filename(info_dict)
                ydl.process_info(info_dict)

            duration_seconds = time_to_seconds(duration)

            caption = (
                f"**Title:** {title}\n"
                f"**Duration:** `{duration}`\n"
                f"**Views:** `{views}`\n"
                f"**Requested by:** {requester}"
            )

            await message.reply_audio(
                audio=audio_file,
                caption=caption,
                performer=client.name,
                thumb=thumb_name,
                title=title,
                duration=duration_seconds,
            )
            await progress_msg.delete()

        except Exception as e:
            await progress_msg.edit(
                f"**Download failed.**\n\nReport this issue at [Support chat](t.me/{SUPPORT_CHAT})\n\n**Error:** {e}"
            )
            print(f"Error downloading song: {e}")

        # Cleanup temporary files
        try:
            if os.path.exists(audio_file):
                os.remove(audio_file)
            if os.path.exists(thumb_name):
                os.remove(thumb_name)
        except Exception as cleanup_error:
            print(f"Cleanup error: {cleanup_error}")

    except Exception as main_error:
        print(f"Main error: {main_error}")
        await message.reply_text(
            "An unexpected error occurred. Please try again or report this issue."
        )
