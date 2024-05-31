from telethon import TelegramClient, events
from Parser import Parser
from Draw import Draw

api_id = 24023329
api_hash = "331c5c7e70b57043e03849acbbc1202a"
user_input_channel = "https://t.me/+diPUlUMl9ns4ODZk"

client = TelegramClient("session_name", api_id, api_hash)
parser = Parser()
draw = Draw()


"""
@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    data = parser.parse_data(event.message.message)

    # create image
    # post to instagram

    # await client.forward_messages(entity="me", messages=event.message)


with client:
    client.run_until_disconnected()
"""


tmp = [
    "Daily income of S-Group for May 28 💸 ",
    "",
    "🔹Profit in S-Forex was +0.19%",
    "",
    "🔹Profit in S-Forex Pro was +0.50%",
    "",
    "🔹 Profit in S-Forex Optimal (I pool) was +0.53%",
    "",
    "🔹 Profit in S-Forex Optimal (II pool) was +0.39%",
    "",
    "🔹Profit in S-Forex Prime was +0.58%",
]
data = parser.parse_data(tmp, True)

draw.draw(data)
