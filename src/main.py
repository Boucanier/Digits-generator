import drawDigits, os, platform

if __name__ == "__main__" :
    if platform.system() == "Windows" :
        os.system("del output\\*.png")
    else :
        os.system("rm output/*.png")
        
    listDigitsImg = list()

    for i in range(10) :
        drawDigits.generateImg(i, 10)