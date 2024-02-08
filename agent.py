from telethon import TelegramClient, events
import re

# Your Telegram API credentials
api_id = '8103298'
api_hash = '1f22d4c5e93a9461c28633251510b4a3'
group_username = 'agent287616289497719993'

# Create a TelegramClient instance
client = TelegramClient('session1', api_id, api_hash)

async def main():
    await client.start()
    print("connected to servers")
    # Fetch the group entity
    global group_entity
    group_entity = await client.get_entity(group_username)

# Function to send message to the group
async def send_message(client, group_entity, message_text):
    await client.send_message(group_entity, message_text)
    print("message sent")

# Define message event handler
@client.on(events.NewMessage)
async def message_handler(event):
    message = event.message
    # Regular expressions to find mobile numbers, usernames, and URLs
    mobile_number_pattern = r'\b(?:\+\d{1,3}[-.●]?)?\(?\d{2,5}\)?[-.●\s]?\d{1,5}[-.●\s]?\d{1,5}[-.●\s]?\d{1,5}\b'
    username_pattern = r'@([A-Za-z0-9_]+)'
    url_pattern = r'(?:\b\w+\.\w+\b|\b\w+\.\w+/\w+\b)'
    wa_me_pattern = r'wa\.me/'
    t_me_pattern = r't\.me/'

    # Compile URL patterns with re.IGNORECASE flag
    url_pattern = re.compile(url_pattern, re.IGNORECASE)
    wa_me_pattern = re.compile(wa_me_pattern, re.IGNORECASE)
    t_me_pattern = re.compile(t_me_pattern, re.IGNORECASE)

    message_text = message.text
    if re.search(mobile_number_pattern, message_text) or re.search(username_pattern, message_text):
        await send_message(client, group_entity, message_text)
    elif re.search(url_pattern, message_text):
        if re.search(wa_me_pattern, message_text) or re.search(t_me_pattern, message_text):
            await send_message(client, group_entity, message_text)

# Run the main function
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()