from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember

@app.on_message(filters.command("staff") & filters.group)
async def staff_list(client: Client, message: Message):
    try:
        # Get the chat administrators
        chat_id = message.chat.id
        chat_admins = await client.get_chat_members(chat_id, filter="administrators")

        # Categorize admins by roles
        owner = []
        co_founders = []
        admins = []

        for member in chat_admins:
            # Fetch user details
            user = member.user
            name = user.first_name
            if user.last_name:
                name += f" {user.last_name}"
            title = member.custom_title or "No Title"
            user_info = f"**Name:** {name}\n**Title:** {title}"

            # Categorize roles
            if member.status == "creator":
                owner.append(user_info)
            elif title.lower() == "co-founder":
                co_founders.append(user_info)
            else:
                admins.append(user_info)

        # Prepare the message
        staff_message = "**👥 Group Staff List:**\n\n"

        if owner:
            staff_message += "**👑 Owner:**\n" + "\n\n".join(owner) + "\n\n"

        if co_founders:
            staff_message += "**🤝 Co-Founders:**\n" + "\n\n".join(co_founders) + "\n\n"

        if admins:
            staff_message += "**🔧 Admins:**\n" + "\n\n".join(admins) + "\n\n"

        # Send the message
        await message.reply_text(staff_message, parse_mode="markdown")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}\nUnable to fetch staff list.", quote=True)
