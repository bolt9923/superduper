from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command("staff") & filters.group)
async def staff_list(client: Client, message: Message):
    try:
        # Fetch the list of administrators
        chat_id = message.chat.id
        chat_admins = []

        async for member in client.get_chat_members(chat_id, filter="administrators"):
            chat_admins.append(member)

        # Categorize admins into roles
        owner = []
        co_founders = []
        admins = []

        for member in chat_admins:
            user = member.user
            name = user.first_name or "Unknown"
            if user.last_name:
                name += f" {user.last_name}"
            title = member.custom_title or "No Title"

            # Categorize based on admin role
            if member.status == "creator":  # Owner of the group
                owner.append(f"**Name:** {name}\n**Title:** {title}")
            elif title.lower() == "co-founder":  # Co-Founder based on custom title
                co_founders.append(f"**Name:** {name}\n**Title:** {title}")
            else:  # Other admins
                admins.append(f"**Name:** {name}\n**Title:** {title}")

        # Build the message
        staff_message = "**👥 Group Staff List:**\n\n"

        if owner:
            staff_message += "**👑 Owner:**\n" + "\n\n".join(owner) + "\n\n"
        if co_founders:
            staff_message += "**🤝 Co-Founders:**\n" + "\n\n".join(co_founders) + "\n\n"
        if admins:
            staff_message += "**🔧 Admins:**\n" + "\n\n".join(admins) + "\n\n"

        if not (owner or co_founders or admins):  # No staff found
            staff_message = "No staff members found in this group."

        # Send the message
        await message.reply_text(staff_message, parse_mode="markdown")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}\nUnable to fetch staff list.", quote=True)
