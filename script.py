import cv2

import sys
import numpy
import time
from pyfirmata import Arduino, util, SERVO

servo_pin = 10;


board = Arduino('COM3')
board.digital[servo_pin].mode = SERVO


def pull_down():
    degree = 70
    board.digital[servo_pin].write(degree)
    time.sleep(degree * 0.002)
    board.digital[servo_pin].write(0)
    time.sleep(degree * 0.002)


numpy.set_printoptions(threshold=sys.maxsize)

def main():
    image = cv2.imread('nishant.png')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    resized = image_resize(bw_image, width=30)
    cv2.imwrite('gray.png', gray_image)
    cv2.imwrite('bw_image.png', bw_image)
    cv2.imwrite('resized.png', resized)
    print_on_console(resized)


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
            if(pixel > 128):
                pull_down()
                board.digital[13].write(1)
                time.sleep(0.1)
                board.digital[13].write(0)
                print('*', end=' ')
            else:
                print(' ', end=' ')
            sys.stdout.flush()
            time.sleep(0.01)
        print()

main()

board.digital[13].write(0)