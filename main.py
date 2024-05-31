import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from classes.Parser import Parser
from classes.Draw import Draw


# load environment variables
load_dotenv()

# get environment variables
API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
USER_INPUT_CHANEL = os.getenv("USER_INPUT_CHANEL", "")
SESSION_NAME = os.getenv("SESSION_NAME", "")

# create classes
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
parser = Parser()
draw = Draw()


# listen for incoming messages on telegram chanel
@client.on(events.NewMessage(chats=USER_INPUT_CHANEL))
async def newMessageListener(event):
    data = parser.parse_data(event.message.message)
    draw.draw(data)

    # create image
    # post to instagram

    # forward message to saved
    # await client.forward_messages(entity="me", messages=event.message)


# run until disconnected
with client:
    client.run_until_disconnected()
