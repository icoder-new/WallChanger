__author__ = 'Ehsonjon Gadoev (aka iCoder-new)'
import ctypes
import glob

def main():
    global pathLen

    folderPath = getPath()
    files = getFiles(folderPath)

    if len(files) > 0:
        picIndex = 0
        print(files[0])
        ui = input("A - Previous\nD - Next\nE - Exit\n")
        while ui != 'E' and ui != 'e':
            picIndex = change(ui, files, picIndex)
            print(files[picIndex])
            ui = input("A - Previous\nD - Next\nE - Exit\n")
    else:
        print("Could not find images!")
    print("Done")

def getPath():
    return input("Enter folder to search images: (e.g. C:/Users/icoder/desktop)\nPath: ")

def getFiles(path):
    temp = glob.glob(path + "/*.jpg")
    tempGlob = glob.glob(path + "/*.png")
    
    for i in range(0, len(tempGlob)):
        temp.append(tempGlob[i])

    del tempGlob
    return temp

def change(ui, files, picIn):
    ind = picIn
    if ui == 'A' or ui == 'a':
        if ind != 0:
            ind -= 1
        else:
            ind = len(files)-1
    elif ui == 'D' or ui == 'd':
        if ind != len(files)-1:
            ind += 1
        else:
            ind = 0
    ctypes.windll.user32.SystemParametersInfoW(20, 0, files[ind], 0)
    return ind

if __name__ == "__main__":
    main()
