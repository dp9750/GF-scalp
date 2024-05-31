from datetime import datetime
from classes.Data import Data


# custom data parser specific to this project
class Parser:

    def parse_data(self, data):
        try:
            data = data.split("\n")
            date = self._get_date(data[0])
            values = [self._get_value(data[i]) for i in range(2, 11, 2)]

            return Data(date, values)
        except Exception as ex:
            print(f"Error getting value: {str(ex)}")
            return None

    def _get_date(self, firstRow):
        try:
            s = "Daily income of S-Group for "
            date = firstRow[len(s) :].split()

            day = date[1]
            month = date[0]
            year = datetime.now().year

            return f"{month} {day}, {year}"
        except Exception as ex:
            print(f"Error parsing date: {str(ex)}")
            return None

    def _get_value(self, s: str) -> str:
        return s.split(" ")[-1][1:-1]
