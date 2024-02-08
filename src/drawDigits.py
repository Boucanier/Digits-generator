from PIL import Image, ImageDraw
import random


def drawDigit(digit: int, img: ImageDraw.ImageDraw) :
    if digit == 0 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((20, 20, 20, 80), fill = "black", width = 4)
        img.line((80, 20, 80, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 1 :
        img.line((50, 20, 50, 80), fill = "black", width = 4)
    elif digit == 2 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((80, 20, 80, 50), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((20, 50, 20, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 3 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((80, 20, 80, 80), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 4 :
        img.line((20, 20, 20, 50), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((80, 20, 80, 80), fill = "black", width = 4)
    elif digit == 5 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((20, 20, 20, 50), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((80, 50, 80, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 6 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((20, 20, 20, 80), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((80, 50, 80, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 7 :
        offSetRightBottom = random.randint(0, 50)
        offSetLeftTop = random.randint(-10, 10)
        offSetMid = random.randint(-10, 10)

        img.line((30, 20 + offSetLeftTop, 80, 20), fill = "black", width = 4)
        img.line((80, 20, 80 - offSetRightBottom, 80), fill = "black", width = 4)
        withBar = random.choice([True, True, False])

        if withBar :
            img.line((50 - offSetRightBottom / 3, 50 - offSetMid, 90 + offSetRightBottom / 3, 50 - offSetMid), fill = "black", width = 4)

    elif digit == 8 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((20, 20, 20, 80), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((80, 20, 80, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
    elif digit == 9 :
        img.line((20, 20, 80, 20), fill = "black", width = 4)
        img.line((20, 20, 20, 50), fill = "black", width = 4)
        img.line((20, 50, 80, 50), fill = "black", width = 4)
        img.line((80, 20, 80, 80), fill = "black", width = 4)
        img.line((20, 80, 80, 80), fill = "black", width = 4)
        