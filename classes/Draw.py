from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from classes.Data import Data


EMPTY_IMG = "imgs/Empty.png"
FONT = "fonts/Barlow-SemiBold.ttf"
FONT_SIZE_DATE = 45
FONT_SIZE_PROFIT = 63
XY_DATE = (400, 570)
X, Y = 755, 815
FILL = (18, 19, 25)
FILL_DATE = (255, 255, 255)
OFFSET = 185
FILE_EXT = ".png"


class Draw:

    def draw(self, data: Data) -> str:

        # Open an Image
        img = Image.open(EMPTY_IMG)

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)

        # Custom font style and font size
        font_date = ImageFont.truetype(FONT, FONT_SIZE_DATE)
        font = ImageFont.truetype(FONT, FONT_SIZE_PROFIT)

        # Add Text to an image
        I1.text(XY_DATE, data.date, font=font_date, fill=FILL_DATE)
        # Incomes
        for i, value in enumerate(data.data):
            I1.text((X, Y + i * OFFSET), value, font=font, fill=FILL)

        # Save the edited image and return the filename
        filename = "imgs/" + data.date + FILE_EXT
        img.save(filename)
        return filename
