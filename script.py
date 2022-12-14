import cv2
import serial
import sys
import numpy
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

numpy.set_printoptions(threshold=sys.maxsize)

# ser = serial.Serial('COM3', 9600, timeout=1)

def main():

    
    # ser.write(b'hello')
    image = cv2.imread('hny.jpg')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    resized = image_resize(bw_image, width=25)
    cv2.imwrite('gray.png', gray_image)
    cv2.imwrite('bw_image.png', bw_image)
    cv2.imwrite('resized.png', resized)
    print_on_console(resized);
    # print(repr(resized))


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

    for row in list_2d:

        for pixel in row:
            print('*' if pixel < 128 else ' ', end=' ')
        print()

# main()

root = tk.Tk()


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename()

    return filename;



print(select_file())