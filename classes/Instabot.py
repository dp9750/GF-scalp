import os
from instabot import Bot


USERNAME = os.getenv("USERNAME", "")
PASSWORD = os.getenv("PASSWORD", "")


class Instabot:

    def __init__(self) -> None:
        self.bot = Bot()

    def login(self):
        self.bot.login(username=USERNAME, password=PASSWORD)

    def logout(self):
        self.bot.logout()

    def upload_story(self, filepath):
        self.bot.upload_story_photo(filepath)
