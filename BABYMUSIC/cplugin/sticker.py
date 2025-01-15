import base64
import httpx
import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import pyrogram
from uuid import uuid4
from config import BOT_USERNAME


######### Sticker ID Command
@Client.on_message(filters.command("st"))
async def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            await client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            await message.reply_text(f"Error: {e}")
    else:
        await message.reply_text("Please provide a sticker ID after the /st command.")


######### Pack Kang Command
@Client.on_message(filters.command("packkang"))
async def _packkang(client: Client, message):
    txt = await message.reply_text("**Processing...**")
    if not message.reply_to_message:
        await txt.edit("Please reply to a message.")
        return
    if not message.reply_to_message.sticker:
        await txt.edit("Please reply to a sticker.")
        return
    if message.reply_to_message.sticker.is_animated or message.reply_to_message.sticker.is_video:
        await txt.edit("Reply to a non-animated, static sticker.")
        return

    # Determine the pack name
    if len(message.command) < 2:
        pack_name = f'{message.from_user.first_name}_sticker_pack_by_@{BOT_USERNAME}'
    else:
        pack_name = message.text.split(maxsplit=1)[1]

    try:
        short_name = message.reply_to_message.sticker.set_name
        stickers = await client.invoke(
            pyrogram.raw.functions.messages.GetStickerSet(
                stickerset=pyrogram.raw.types.InputStickerSetShortName(short_name=short_name),
                hash=0
            )
        )

        shits = stickers.documents
        sticks = []
        for i in shits:
            sex = pyrogram.raw.types.InputDocument(
                id=i.id,
                access_hash=i.access_hash,
                file_reference=i.file_reference
            )
            sticks.append(
                pyrogram.raw.types.InputStickerSetItem(
                    document=sex,
                    emoji=i.attributes[1].alt
                )
            )

        short_name = f'sticker_pack_{str(uuid4()).replace("-", "")}_by_{BOT_USERNAME}'
        user_id = await client.resolve_peer(message.from_user.id)

        # Create the new sticker set
        await client.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks,
            )
        )
        await txt.edit(
            f"**Sticker pack created!**\n**Total stickers:** {len(sticks)}",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Pack link", url=f"http://t.me/addstickers/{short_name}")]]
            )
        )
    except Exception as e:
        await txt.edit(f"Error: {e}")


######### Sticker ID Command
@Client.on_message(filters.command(["stickerid", "stid"]))
async def sticker_id(client: Client, message):
    if not message.reply_to_message:
        await message.reply_text("Please reply to a sticker.")
        return
    if not message.reply_to_message.sticker:
        await message.reply_text("Please reply to a sticker.")
        return

    sticker = message.reply_to_message.sticker
    await message.reply_text(f"""
⊹ <u>**Sticker Info**</u> ⊹
**Sticker ID:** `{sticker.file_id}`
**Sticker Unique ID:** `{sticker.file_unique_id}`
""")
