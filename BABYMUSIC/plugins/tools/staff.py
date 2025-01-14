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

        # Prepare a response message
        staff_message = "**👥 Group Staff List:**\n\n"

        # Process each admin and organize them by their roles
        owner_found = False
        co_founder_found = False
        admin_found = False

        for member in chat_admins:
            user = member.user
            name = user.first_name or "Unknown"
            if user.last_name:
                name += f" {user.last_name}"

            # Check if the user is the owner (creator of the group)
            if member.status == "creator" and not owner_found:
                staff_message += f"**👑 Owner:**\n**Name:** {name}\n**Title:** Group Owner\n\n"
                owner_found = True

            # Check if the user has a custom title like "Co-Founder"
            elif member.status == "administrator" and "co-founder" in (member.custom_title or "").lower() and not co_founder_found:
                staff_message += f"**🤝 Co-Founder:**\n**Name:** {name}\n**Title:** Co-Founder\n\n"
                co_founder_found = True

            # Add the user as a regular admin
            elif member.status == "administrator" and not admin_found:
                staff_message += f"**🔧 Admin:**\n**Name:** {name}\n**Title:** {member.custom_title or 'No Title'}\n\n"
                admin_found = True

        if not (owner_found or co_founder_found or admin_found):  # No staff members found
            staff_message = "No staff members found in this group."

        # Send the result to the chat
        await message.reply_text(staff_message, parse_mode="markdown")
        
    except Exception as e:
        # Error handling if something goes wrong
        error_message = f"Error: {str(e)}" 
        await message.reply_text(error_message, quote=True)
