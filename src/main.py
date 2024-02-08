import drawDigits, os

if __name__ == "__main__" :
    os.system("rm output/*.png")
    listDigitsImg = list()

    for i in range(10) :
        drawDigits.generateImg(i, 10)