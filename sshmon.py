#must have webhook url in .env file as "whurl=https://webhookyboi.com/burblgurgle"

import os
import asyncio
from discord_webhook import DiscordWebhook

from dotenv import load_dotenv

load_dotenv()
whurl = os.getenv('whurl')

LOG_FILE = "/var/log/auth.log"
print(f'running...')

# Words to search for in the log file
SEARCH_WORDS = ['Accepted', 'Disconnected', 'systemd-logind', 'failed', 'failures']

# Keep track of the last position in the file
last_position = os.path.getsize(LOG_FILE)
print(f'{last_position}')
# Check for new lines containing the search words in the log file
async def check_log_file():
    global last_position
    while True:
        with open(LOG_FILE, 'r') as file:
            file.seek(last_position)
            line = file.readline().strip()
            while line:
                if any(word in line.lower() for word in SEARCH_WORDS):
                    await send_log_message(line)
                line = file.readline().strip()
            last_position = file.tell()
        await asyncio.sleep(1)

# Send the log message to the designated channel
async def send_log_message(message):
     webhook = DiscordWebhook(url=whurl, content=message)
     response = webhook.execute()

asyncio.run(check_log_file())
