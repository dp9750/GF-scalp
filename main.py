import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from classes.Parser import Parser
from classes.Draw import Draw

load_dotenv()

api_id = os.getenv("API_ID", "")
api_hash = os.getenv("API_HASH", "")
user_input_channel = os.getenv("USER_INPUT_CHANEL", "")

client = TelegramClient("session_name", api_id, api_hash)
parser = Parser()
draw = Draw()


@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    data = parser.parse_data(event.message.message)
    draw.draw(data)

    # create image
    # post to instagram

    # await client.forward_messages(entity="me", messages=event.message)


with client:
    client.run_until_disconnected()
