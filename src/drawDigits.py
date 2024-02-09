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
        bottomToTop = random.choice(list(range(30,100,5)))
        img.ellipse((L+bottomToTop, T, R-bottomToTop, B), fill="white", outline="black", width=random.randint(3,6))
    elif digit == 1 :
        offSetMainBarBot = random.choice(list(range(-1,2)))
        img.line((W * 12/20, T, W * (12+offSetMainBarBot)/20, B), fill = "black", width = random.randint(3, 6))
    elif digit == 2 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, L, B), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 3 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R, B), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 4 :
        img.line((L, T, L, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 5 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((L, T, L, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((R, H * 5/10, R, B), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 6 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((L, T, L, B), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((R, H * 5/10, R, B), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 7 :
        offSetRightBottom = random.randint(0, W * 5/10)
        offSetLeftTop = random.randint(-H * 1/10, H * 1/10)
        offSetMid = random.randint(-W * 3/100, W * 3/100)

        img.line((W * 3/10, T + offSetLeftTop, R, T), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R - offSetRightBottom, B), fill = "black", width = random.randint(3, 6))
        withBar = random.choice([True, True, True, False])

        if withBar :
            img.line((W * 5/10 - offSetRightBottom / 3, H * 5/10 - offSetMid, R + offSetRightBottom / 3, H * 5/10 + offSetMid), fill = "black", width = random.randint(3, 6))

    elif digit == 8 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((L, T, L, B), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R, B), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))
    elif digit == 9 :
        img.line((L, T, R, T), fill = "black", width = random.randint(3, 6))
        img.line((L, T, L, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((L, H * 5/10, R, H * 5/10), fill = "black", width = random.randint(3, 6))
        img.line((R, T, R, B), fill = "black", width = random.randint(3, 6))
        img.line((L, B, R, B), fill = "black", width = random.randint(3, 6))


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