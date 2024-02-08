from PIL import Image, ImageDraw
import random

# Height
H = 500

# Width
W = 500

# Margin
M = 70

# Bottom y coordinate
B = H - M

# Right x coordinate
R = W - M

# Top y and left x coordinate
T = L = M

def drawDigit(digit: int, img: ImageDraw.ImageDraw) -> None:
    if digit == 0 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((L, T, L, B), fill = "black", width = 4)
        img.line((R, T, R, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 1 :
        img.line((W * 5/10, T, W * 5/10, B), fill = "black", width = 4)
    elif digit == 2 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((R, T, R, H * 5/10), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((L, H * 5/10, L, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 3 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((R, T, R, B), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 4 :
        img.line((L, T, L, H * 5/10), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((R, T, R, B), fill = "black", width = 4)
    elif digit == 5 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((L, T, L, H * 5/10), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((R, H * 5/10, R, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 6 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((L, T, L, B), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((R, H * 5/10, R, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 7 :
        offSetRightBottom = random.randint(0, 50)
        offSetLeftTop = random.randint(-10, 10)
        offSetMid = random.randint(-3, 3)

        img.line((W * 3/10, T + offSetLeftTop, R, T), fill = "black", width = 4)
        img.line((R, T, R - offSetRightBottom, B), fill = "black", width = 4)
        withBar = random.choice([True, True, True, False])

        if withBar :
            img.line((W * 5/10 - offSetRightBottom / 3, H * 5/10 - offSetMid, R + offSetRightBottom / 3, H * 5/10 + offSetMid), fill = "black", width = 4)

    elif digit == 8 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((L, T, L, B), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((R, T, R, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)
    elif digit == 9 :
        img.line((L, T, R, T), fill = "black", width = 4)
        img.line((L, T, L, H * 5/10), fill = "black", width = 4)
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = 4)
        img.line((R, T, R, B), fill = "black", width = 4)
        img.line((L, B, R, B), fill = "black", width = 4)


def generateImg(num: int, n: int) -> None:
    """
        Generate n images of digit num

        - Args:
            - num: int
                The digit to draw
            - n: int
                The number of images to generate
    """
    for i in range(n):
        img = Image.new('L', (W, H), color = "white")
        drawDigit(num, ImageDraw.Draw(img))
        img.save("output/numero-" + str(num) + "-" + str(i) + ".png")