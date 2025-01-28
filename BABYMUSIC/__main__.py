import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BABYMUSIC import LOGGER, app, userbot
from BABYMUSIC.ccore.Cuserbot import start_all_assistants
from BABYMUSIC.core.call import BABY
from BABYMUSIC.misc import sudo
from BABYMUSIC.plugins import ALL_MODULES
from BABYMUSIC.utils.database import get_banned_users, get_gbanned
from BABYMUSIC.plugins.tools.clone import restart_bots  # Import start_all_assistants
from config import BANNED_USERS

async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please provide a valid session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()

    # Import all modules dynamically
    for all_module in ALL_MODULES:
        importlib.import_module("BABYMUSIC.plugins" + all_module)

    LOGGER("BABYMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    await userbot.start()
    await BABY.start()

    # Start the voice chat if available
    try:
        await BABY.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("BABYMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass

    # Call the function to start all assistants
    await start_all_assistants()  # Start all the assistants

    await BABY.decorators()
    await restart_bots()
    LOGGER("BABYMUSIC").info(
        "CONTACT ︎MADE BY UNTOLDCODER"
    )

    # Idle to keep the app running
    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("BABYMUSIC").info("𝗦𝗧𝗢𝗣 𝗣𝗿𝗼𝗕𝗼𝘁 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
