from instabot import Bot


class Instabot:

    def __init__(self) -> None:
        self.bot = Bot()

    def login(self, username, password):
        self.bot.login(username=username, password=password)

    def logout(self):
        self.bot.logout()

    def upload_story(self, filepath):
        self.bot.upload_story_photo(filepath)
