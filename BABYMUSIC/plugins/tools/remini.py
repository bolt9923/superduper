import base64
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
import os
from config import BANNED_USERS
from BABYMUSIC import app

@app.on_message(filters.command(["remini", "enhance"]) & filters.private & ~BANNED_USERS)
async def upscale_image(client: Client, message: Message):
    try:
        # Check if the command is a reply to a photo
        if message.reply_to_message and message.reply_to_message.photo:
            progress_msg = await message.reply_text(
                "Enhancing your image, please wait..."
            )

            # Download the photo
            photo = message.reply_to_message.photo[-1]
            image_path = await client.download_media(photo.file_id)

            # Read and encode the image in base64
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
            b64_image = base64.b64encode(image_data).decode("utf-8")

            # Send the image to the upscaling API
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    "https://lexica.qewertyy.dev/upscale",
                    json={"image_data": b64_image},
                ) as response:
                    if response.status == 200:
                        upscaled_image = await response.read()
                        upscaled_file_path = "upscaled_image.png"

                        # Save the upscaled image
                        with open(upscaled_file_path, "wb") as output_file:
                            output_file.write(upscaled_image)

                        # Delete the progress message
                        await progress_msg.delete()

                        # Send the upscaled image to the user
                        await message.reply_document(
                            document=open(upscaled_file_path, "rb"),
                            caption=f"<b>Enhanced your image.</b>\n<b>Enhanced By:</b> @{client.me.username}",
                            parse_mode=ParseMode.HTML,
                        )

                        # Clean up temporary files
                        os.remove(image_path)
                        os.remove(upscaled_file_path)
                    else:
                        await progress_msg.delete()
                        raise Exception(f"Upscaling failed with status code {response.status}")
        else:
            await message.reply_text("Please reply to an image to upscale it.")

    except Exception as e:
        logger.error(f"Failed to upscale the image: {e}")
        await message.reply_text(
            "Failed to upscale the image. Please try again later."
        )
