from datetime import datetime


class Parser:

    def parse_data(self, data, test=False):
        try:
            if not test:
                data = data.split("\n")

            date = self.get_date(data[0])

            return {
                "date": date,
                "forex": self.get_value(data[2]),
                "pro": self.get_value(data[4]),
                "optimal1": self.get_value(data[6]),
                "optimal2": self.get_value(data[8]),
                "prime": self.get_value(data[10]),
            }

        except Exception:
            return None

    def get_date(self, firstRow):
        s = "Daily income of S-Group for "
        date = firstRow[len(s) :].split()

        day = date[1]
        month = date[0]
        year = datetime.now().year

        return f"{month} {day}, {year}"

    def get_value(self, s: str) -> str:
        return s.split(" ")[-1][1:-1]
