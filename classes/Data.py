# custom data class specifily for the project data
class Data:
    def __init__(
        self, date: str, forex: str, pro: str, optimal1: str, optimal2: str, prime: str
    ):
        self.date = date
        self.data = [forex, pro, optimal1, optimal2, prime]
