from BABYMUSIC import app
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, enums
from logging import getLogger

LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        """Check the welcome notification state for a chat."""
        return self.data.get(chat_id, {"state": "on"})  # Default state is "on"

    async def set_state(self, chat_id, state):
        """Set the state of welcome notifications for a chat."""
        self.data[chat_id] = {"state": state}

wlcm = WelDatabase()

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n`/welcome [on|off]`"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    
    chat_id = message.chat.id
    user = await app.get_chat_member(chat_id, message.from_user.id)
    
    if user.status not in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        return await message.reply("**You need to be an admin to do this.!**")
    
    state = message.text.split(None, 1)[1].strip().lower()
    if state not in ["on", "off"]:
        return await message.reply_text(usage)
    
    current_state = await wlcm.find_one(chat_id)
    if current_state["state"] == state:
        return await message.reply_text(
            f"**Welcome notifications are already `{state}` for this chat!**"
        )
    
    # Update the state in the database
    await wlcm.set_state(chat_id, state)
    await message.reply_text(
        f"**Welcome notifications have been turned `{state}` in {message.chat.title}.**"
    )

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    welcome_state = await wlcm.find_one(chat_id)

    # Skip sending welcome messages if the state is "off"
    if welcome_state["state"] == "off":
        return

    user = member.new_chat_member.user if member.new_chat_member else None
    if not user:
        return

    try:
        count = await app.get_chat_members_count(chat_id)
        welcome_message = (
            f"**Hey {user.mention} how are you?, Welcome to {member.chat.title}!\n\n"
            "• I hope you are doing well!\n"
            "• Please make sure to follow the group rules.\n"
            "────────────────────\n"
            f"Total Members: {count}\n"
            "────────────────────**"
        )
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Join 👋", url="https://t.me/BABY09_WORLD")]]
        )
        await app.send_message(chat_id, welcome_message, reply_markup=keyboard)
    except Exception as e:
        LOGGER.error(f"Error sending welcome message: {e}")
