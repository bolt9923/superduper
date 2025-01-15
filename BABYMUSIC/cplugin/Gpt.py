import requests
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters

# Replace with your API key
API_KEY = "abacf43bf0ef13f467283e5bc03c2e1f29dae4228e8c612d785ad428b32db6ce"
BASE_URL = "https://api.together.xyz/v1/chat/completions"

@Client.on_message(
    filters.command(
        ["chatgpt", "ai", "ask", "gpt", "solve"],
        prefixes=["+", ".", "/", "-", "$", "#", "&"],
    )
)
async def chat_gpt(bot, message: Message):
    try:
        # Indicate typing action
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            # Send usage example if no query is provided
            await message.reply_text(
                "Example:\n\n`/gpt Where is the Taj Mahal?`"
            )
            return

        # Extract the user's query
        query = message.text.split(' ', 1)[1]
        print("Input query:", query)  # Debugging input

        # Set headers and payload for the API request
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }

        # Send POST request to the API
        response = requests.post(BASE_URL, json=payload, headers=headers)

        # Check the API response
        if response.status_code != 200:
            await message.reply_text(f"Error: API request failed with status code {response.status_code}.")
            return

        # Parse the JSON response
        response_data = response.json()
        print("API Response JSON:", response_data)  # Debugging response JSON

        if "choices" in response_data and len(response_data["choices"]) > 0:
            result = response_data["choices"][0]["message"]["content"].strip()
            if result:
                await message.reply_text(
                    f"{result}\n\nQuery by @{bot.username}",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                await message.reply_text("Error: Received an empty response from the API.")
        else:
            await message.reply_text("Error: API did not return any choices.")
    except Exception as e:
        # Handle unexpected exceptions
        await message.reply_text(f"An error occurred:\n\n`{e}`")
