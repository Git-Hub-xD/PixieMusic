from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from ANNIEMUSIC import app


@app.on_message(filters.command("population"))
def country_command_handler(client: Client, message: Message):
    # Extract the country code from the command
    country_code = message.text.split(maxsplit=1)[1].strip()

    # Call the external API for country information
    api_url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        country_info = response.json()
        if country_info:
            # Extract relevant information from the API response
            country_name = country_info[0].get("name", {}).get("common", "N/A")
            capital = country_info[0].get("capital", ["N/A"])[0]
            population = country_info[0].get("population", "N/A")

            response_text = (
                f"**ᴄᴏᴜɴᴛʀʏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :**\n\n"
                f"ɴᴀᴍᴇ: {country_name}\n"
                f"ᴄᴀᴘɪᴛᴀʟ: {capital}\n"
                f"ᴘᴏᴘᴜʟᴀᴛɪᴏɴ: {population}"
            )
        else:
            response_text = "ᴇʀʀᴏʀ ғᴇᴛᴄʜɪɴɢ ᴄᴏᴜɴᴛʀʏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴛʜᴇ ᴀᴘɪ."
    except requests.exceptions.HTTPError as http_err:
        response_text = f"ʜᴛᴛᴘ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ ᴇɴᴛᴇʀ ᴄᴏʀʀᴇᴄᴛ ᴄᴏᴜɴᴛʀʏ ᴄᴏᴅᴇ"
    except Exception as err:
        response_text = f" ᴇᴇʀᴏʀ @XovaAssociation"

    # Send the response to the Telegram chat
    message.reply_text(response_text)
