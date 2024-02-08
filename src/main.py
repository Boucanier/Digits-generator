from drawDigits import *

if __name__ == "__main__" :
    listDigitsImg = list()

    for i in range(10) :
        img = Image.new('L', (100, 100), color = "white")
        drawDigit(i, ImageDraw.Draw(img))
        img.save("output/numero-" + str(i) + ".png")