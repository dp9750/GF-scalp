import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from classes.Parser import Parser
from classes.Draw import Draw
from classes.Instabot import Instabot


# load environment variables
load_dotenv()

# get environment variables
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
USER_INPUT_CHANEL = os.getenv("USER_INPUT_CHANEL", "")
SESSION_NAME = os.getenv("SESSION_NAME", "")
USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")

# Create classes
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
parser = Parser()
draw = Draw()
insta = Instabot()


# listen for incoming messages on telegram chanel
@client.on(events.NewMessage(chats=USER_INPUT_CHANEL))
async def newMessageListener(event):
    data = parser.parse_data(event.message.message)
    path = draw.draw(data)

    # Upload instagram story
    insta.login()
    insta.upload_story(path)
    insta.logout()

    # Send converted image to the converts channel
    await client.send_file(entity=USER_INPUT_CHANEL, file=open(path, "rb"))

    # Delete file after it is used
    if os.path.exists(path):
        os.remove(path)


# Run until disconnected
with client:
    client.run_until_disconnected()
