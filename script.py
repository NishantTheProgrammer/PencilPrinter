import cv2
import serial
import sys
import numpy
import time
from waiting import wait
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

numpy.set_printoptions(threshold=sys.maxsize)

ser = serial.Serial('COM3', 9600, write_timeout=0, timeout=None)
time.sleep(5)

def main():
    image = cv2.imread('square.jpg')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    resized = image_resize(bw_image, width=15)
    cv2.imwrite('gray.png', gray_image)
    cv2.imwrite('bw_image.png', bw_image)
    cv2.imwrite('resized.png', resized)
    print_on_console(resized);


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized



def print_on_console(list_2d):
    for y, row in enumerate(list_2d, start=1):
        for x, pixel in enumerate(row, start=1):
            sys.stdout.flush()
            if(pixel < 128):
                gotoDot(x if y % 2 == 0 else len(row) - x + 1 , y)
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename()

    return filename;

def left():
    ser.write(b'left')
    wailForExcecute()
def right():
    ser.write(b'right')
    wailForExcecute()
def top():
    ser.write(b'top')
    wailForExcecute()
def bottom():
    ser.write(b'bottom')
    wailForExcecute()

def pullDown():
    ser.write(b'pullDown')
    wailForExcecute()

def gotoDot(x, y):
    print(f'gotoDot_{x}_{y}')
    ser.write(f'gotoDot_{x}_{y}'.encode())
    wailForExcecute()

def wailForExcecute():
    wait(lambda : ser.in_waiting)
    ser.flushInput()
    time.sleep(0.5)
main()










# root = tk.Tk()        
