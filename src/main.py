import drawDigits, os, platform

if __name__ == "__main__" :
    if not os.path.exists("output") :
        os.mkdir("output")
    if platform.system() == "Windows" :
        os.system("del output\\*.png")
    else :
        os.system("rm output/*.png")

    for i in range(10) :
        drawDigits.generateImg(i, 10)
