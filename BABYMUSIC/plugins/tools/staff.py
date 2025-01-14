from BABYMUSIC import app
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command("staff") & filters.group)
async def staff_list(client: Client, message: Message):
    try:
        # Fetch the list of administrators
        chat_id = message.chat.id
        chat_admins = []

        # Get all the admins in the group
        async for member in client.get_chat_members(chat_id, filter="administrators"):
            chat_admins.append(member)

        # Categorize admins by roles
        owner = []
        co_founders = []
        admins = []

        for member in chat_admins:
            user = member.user
            name = user.first_name or "Unknown"
            if user.last_name:
                name += f" {user.last_name}"
            title = member.custom_title or "No Title"

            # Categorize based on member status
            if member.status == "creator":  # Group Owner
                owner.append(f"**Name:** {name}\n**Title:** {title}")
            elif member.status == "administrator":  # Admin role
                if title.lower() == "co-founder":  # Check for custom title
                    co_founders.append(f"**Name:** {name}\n**Title:** {title}")
                else:
                    admins.append(f"**Name:** {name}\n**Title:** {title}")

        # Build the response message
        staff_message = "**👥 Group Staff List:**\n\n"

        if owner:
            staff_message += "**👑 Owner:**\n" + "\n\n".join(owner) + "\n\n"
        if co_founders:
            staff_message += "**🤝 Co-Founders:**\n" + "\n\n".join(co_founders) + "\n\n"
        if admins:
            staff_message += "**🔧 Admins:**\n" + "\n\n".join(admins) + "\n\n"

        if not (owner or co_founders or admins):  # No staff members
            staff_message = "No staff members found in this group."

        # Send the result to the chat
        await message.reply_text(staff_message, parse_mode="markdown")
        
    except Exception as e:
        # Error handling if something goes wrong
        await message.reply_text(f"Error: {str(e)}\nUnable to fetch staff list.", quote=True)
