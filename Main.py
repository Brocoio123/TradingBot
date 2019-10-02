from tkinter import *
from tkfilebrowser import askopendirname, askopenfilenames, asksaveasfilename
from PIL import Image, ImageTk
import pytesseract
import os
from PIL import ImageGrab
import win32gui
import json
from datetime import datetime
import pyautogui
import random
import scipy
import time
from scipy import interpolate

arrayCoordinates = []
#arrayCoordinates:ne
arrayCoordinates = [(978.0, 256.0), (1032.0, 293.0), (955.0, 296.0), (1028.0, 330.0), (946.0, 339.0), (1029.0, 371.0)]
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Everardo\AppData\Local\Tesseract-OCR\tesseract.exe"
hastyped = ""

def average_price_yesterday():
    with open("prices.json", 'r') as f:
        datastore = json.load(f)
    #average =

# precisa de trabalho, não faz uma curva
def move_mouse_human(movetox, movetoy):
    cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
    x1, y1 = pyautogui.position()  # Starting position
    x2, y2 = movetox, movetoy  # Destination

    # Distribute control points between start and destination evenly.
    x = scipy.linspace(x1, x2, num=cp, dtype='int')
    y = scipy.linspace(y1, y2, num=cp, dtype='int')

    # Randomise inner points a bit (+-RND at most).
    RND = 10
    xr = scipy.random.randint(-RND, RND, size=cp)
    yr = scipy.random.randint(-RND, RND, size=cp)
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    # Approximate using Bezier spline.
    degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
    # Must be less than number of control points.
    tck, u = scipy.interpolate.splprep([x, y], k=degree)
    u = scipy.linspace(0, 1, num=max(pyautogui.size()))
    points = scipy.interpolate.splev(u, tck)

    # Move mouse.
    duration = random.uniform(0.0, 0.4)
    timeout = duration / len(points[0])
    for point in zip(*(i.astype(int) for i in points)):
        pyautogui.platformModule._moveTo(int(point[0]), int(point[1]))
        time.sleep(timeout)
    time.sleep(0.5)


def click():
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.4)

#def mouse_move_check_duplicate_item():


def keyboard_type_human(stringType):
    for character in stringType:
        randomduration = random.uniform(0.0, 0.3)
        pyautogui.typewrite(character, randomduration)
    return stringType


def save_To_Json(dictionary):
    with open('prices.json', 'a') as json_file:
        json.dump(dictionary, json_file, indent=4, sort_keys=True)


def take_Screenshot(path):
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

    win32gui.EnumWindows(enum_cb, toplist)

    dofus = [(hwnd, title) for hwnd, title in winlist if 'dofus' in title.lower()]
    # just grab the hwnd for first window matching firefox
    dofus = dofus[0]
    hwnd = dofus[0]

    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(bbox)
    img.save(path, img.format, quality='keep')


def ocr_core(filename):
    text = pytesseract.image_to_string((Image.open(filename)), lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    print(text)
    print("OCR")
    return text


# as instrucoes
def returntypedstring(sourceVal, varToSet):
    sourceVal = varToSet

def backspace():
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')
    pyautogui.press('backspace')


# input:nom de l'item. output:prix pous 1,10 et 100 items
def perform_item_capture(itemCaptured):


    take_Screenshot('Capture.png')
    count1 = 0
    count10 = 0
    count100 = 0
    if os.path.exists("Capture.png"):
        i = 0
        e = -1
        file_num = 0
        while (i < len(arrayCoordinates) / 2):
            img = Image.open('Capture.png')
            if i % 2 == 0:
                imgTemp = img.crop((arrayCoordinates[i + i][0], arrayCoordinates[i + i][1],
                                    arrayCoordinates[i + i + 1][0], arrayCoordinates[i + i + 1][1]))
            else:
                imgTemp = img.crop((arrayCoordinates[i + i][0], arrayCoordinates[i + i][1],
                                    arrayCoordinates[i + i + 1][0], arrayCoordinates[i + i + 1][1]))
                e = e + 1
            width, height = imgTemp.size
            width = width * 2
            height = height * 2
            imgTemp = imgTemp.resize((width, height), Image.ANTIALIAS)
            imgTemp.save("Screenshot/" + str(i) + ".png", imgTemp.format, quality='keep')
            time.sleep(1)

            # ver se da pra optimisar dps
            if i == 0:
                count1 = ocr_core("Screenshot/" + str(file_num) + ".png")
            elif i == 1:
                count10 = ocr_core("Screenshot/" + str(file_num) + ".png")
            elif i == 2:
                count100 = ocr_core("Screenshot/" + str(file_num) + ".png")

            time.sleep(0.3)
            os.remove("Screenshot/" + str(i) + ".png")

            i = i + 1
            file_num = file_num + 1
            time.sleep(1)

        item_price = {
            itemCaptured: [count1, count10, count100]
        }

        time.sleep(1)
        os.remove("Capture.png")
    return item_price


def login ():
    move_mouse_human(903, 419)
    click()
    keyboard_type_human("Dado1241942")
    time.sleep(1)
    move_mouse_human(959, 570)
    click()
    time.sleep(20)
    move_mouse_human(816, 531)
    click()

def is_rentable():
    print("yes")
#lowest price per bulk per unit
def bulkBuY(p1, p10, p100):
    #while()
    b = "1"
    if p10/10 < p1:
        b = "10"

    if p100/100 < p10:
        b = "100"

    return b

def movementScript():
    i = 0
    currentItem = ""
    #login()

    with open("items.json", 'r') as f:
        items = json.load(f)

    while i < len(items):
        currentItem = items[str(i)]
        datetimeobj = datetime.now()
        if not os.path.exists("json/"+currentItem+".json"):
            with open("json/" + currentItem + ".json", 'w+') as f:
                f.write("{}")
            with open("json/" + currentItem + ".json", 'r') as f:
                json_string = json.load(f)
        else:
            with open("json/"+currentItem+".json", 'r') as f:
                json_string = json.load(f)

        if bool(json_string) == False:
            print("IFFFFFFF")
            json_string = {str(datetimeobj.day): {
                str(datetimeobj.hour): {

                }
            }}
        else:
            print("ELSEEEEEE")
            # json_string = oldJson
            a = 0
            print(json.dumps(json_string, indent=4, sort_keys=True))

            json_string[str(datetimeobj.day)][str(datetimeobj.hour)] = {

            }
        print(json_string)
        move_mouse_human(520, 212)
        #time.sleep(0.8)
        click()
        backspace()
        itemCaptured = keyboard_type_human(currentItem)
        move_mouse_human(730, 229)
        click()
        time.sleep(1)
        stringAppend = perform_item_capture(itemCaptured)
        print(json_string)
        print(stringAppend)
        json_string[str(datetimeobj.day)][str(datetimeobj.hour)] = stringAppend
        with open("json/"+currentItem+'.json', 'w') as json_file:
            json.dump(json_string, json_file, indent=4, sort_keys=True)
        i = i + 1

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.button1 = Button(self.frame, text='Text Positions', width=25, command=self.new_window)
        self.button1.pack()
        self.button2 = Button(self.frame, text='New Window', width=25, command=self.new_window)
        self.button2.pack()
        self.button3 = Button(self.frame, text='Run', width=25, command=self.ocr_run)
        self.button3.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = ImageCanvasWindow(self.newWindow)

    def ocr_run(self):
        # os.remove("Sample_screen.png")
        dayElapse = 0

        while True:
            movementScript()
            time.sleep(3600)
            dayElapse = dayElapse + 1
            # if dayElapse == 24:


class ImageCanvasWindow:
    def __init__(self, master):
        self.master = master
        take_Screenshot("Sample_screen.png")
        time.sleep(1)
        # setting up a tkinter canvas with scrollbars
        frame = Frame(self.master, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        xscroll = Scrollbar(frame, orient=HORIZONTAL)
        xscroll.grid(row=1, column=0, sticky=E + W)
        yscroll = Scrollbar(frame)
        yscroll.grid(row=0, column=1, sticky=N + S)
        canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        canvas.grid(row=0, column=0, sticky=N + S + E + W)
        xscroll.config(command=canvas.xview)
        yscroll.config(command=canvas.yview)
        frame.pack(fill=BOTH, expand=1)

        # adding the image
        img = ImageTk.PhotoImage(Image.open('Sample_screen.png'))
        canvas.create_image(0, 0, image=img, anchor="nw")
        canvas.config(scrollregion=canvas.bbox(ALL))

        # function to be called when mouse is clicked
        def printcoords(event):
            # outputting x and y coords to console
            print(canvas.canvasx(event.x), canvas.canvasy(event.y))
            arrayCoordinates.append((canvas.canvasx(event.x), canvas.canvasy(event.y)))
            # print(arrayCoordinates)

        canvas.bind("<Button 1>", printcoords)

        # Por alguma razão o erro faz com que a imagem apareca, corrijo depois
        img_canvas.qualquercoisa()


def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
