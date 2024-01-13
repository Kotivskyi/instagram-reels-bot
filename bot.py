import asyncio
import telethon

from telethon import TelegramClient, events

# Replace this with your bot's token
import os

bot_token = os.environ["BOT_TOKEN"]

# Create the Telegram client
client = TelegramClient("bot", bot_token=bot_token)

async def main():
    # Start the bot
    await client.start()

    # Register the message handler
    @client.on(events.NewMessage)
    async def handle_message(event):
        if "www.instagram.com/reel" in event.text:
            updated_message = event.text.replace("www.instagram.com/reel", "www.instagram.com/reel")
            await event.reply(updated_message)

    # Run the bot until you press Ctrl-C
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())