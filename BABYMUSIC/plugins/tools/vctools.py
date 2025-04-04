from pyrogram import Client, filters
from pyrogram.types import Message
from BABYMUSIC import app
from pyrogram import *
from pyrogram.types import *
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall
from BABYMUSIC.utils.database import get_assistant
from telethon.tl.functions.phone import (
    CreateGroupCallRequest,
    DiscardGroupCallRequest,
    GetGroupCallRequest,
    InviteToGroupCallRequest,
)

from pyrogram.raw import functions, types
from asyncio import sleep

@app.on_raw_update()
async def on_voice_chat_participant_update(client: Client, update, users, chats):
    # Check if the raw update is related to group call participants
    if isinstance(update, types.UpdateGroupCallParticipants):
        for participant in update.participants:
            # Check if the participant just joined the call
            if isinstance(participant, types.GroupCallParticipant) and not participant.left:
                try:
                    # Fetch user details
                    user = await client.get_users(participant.user_id)
                    if user:
                        name = user.first_name
                        user_id = user.id

                        # Send notification message
                        msg = await client.send_message(
                            chat_id=update.peer.channel_id,
                            text=f"📢 **User Joined Voice Chat:**\n\n**Name:** {name}\n**User ID:** `{user_id}`"
                        )
                        # Delete the message after 5 seconds
                        await sleep(5)
                        await msg.delete()
                except Exception as e:
                    print(f"Error: {e}")



# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    await msg.reply("**⌯ ◉ 𝗩𝗖 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ◉ ⌯**")


# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    await msg.reply("**⌯ ◉ 𝗩𝗖 𝗘𝗡𝗗𝗘𝗗 ◉ ⌯**")


# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"➻ {message.from_user.mention}\n\n**๏ ɪɴᴠɪᴛɪɴɢ ɪɴ ᴠᴄ ᴛᴏ :**\n\n**➻ **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        reply_text = f"{text} 🤭🤭"

        await message.reply(
            reply_text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="๏ ᴊᴏɪɴ ᴠᴄ ๏", url=add_link)],
                ]
            ),
        )
    except Exception as e:
        print(f"Error: {e}")


####


@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):
    expression = message.text.split("/math ", 1)[1]
    try:
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(
            f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
            headers={"x-referer": "https://explorer.apis.google.com"},
        ) as r:
            response = await r.json()
            result = ""

            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r"\/\d", item["link"]):
                    link = re.sub(r"\/\d", "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [
                Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")
            ]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
