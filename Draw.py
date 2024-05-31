from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

EMPTY_IMG = "Empty.png"
FONT = "fonts/Barlow-SemiBold.ttf"
FONT_SIZE_DATE = 45
FONT_SIZE_PROFIT = 63
X, Y = 755, 815
FILL = (18, 19, 25)


class Draw:

    def draw(self, data):

        # Open an Image
        img = Image.open(EMPTY_IMG)

        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)

        # Custom font style and font size
        font_date = ImageFont.truetype(FONT, FONT_SIZE_DATE)
        font = ImageFont.truetype(FONT, FONT_SIZE_PROFIT)

        # Add Text to an image
        I1.text((400, 570), data["date"], font=font_date, fill=(255, 255, 255))
        I1.text((X, Y), data["forex"], font=font, fill=FILL)
        I1.text((X, Y + 185), data["pro"], font=font, fill=FILL)
        I1.text((X, Y + 2 * 185), data["optimal1"], font=font, fill=FILL)
        I1.text((X, Y + 3 * 185), data["optimal2"], font=font, fill=FILL)
        I1.text((X, Y + 4 * 185), data["prime"], font=font, fill=FILL)

        # Display edited image
        # img.show()

        # Save the edited image
        filename = data["date"] + ".png"
        img.save(filename)
