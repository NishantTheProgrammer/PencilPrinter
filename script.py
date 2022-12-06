import cv2

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

def main():
    image = cv2.imread('bird.jpeg')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    resized = image_resize(bw_image, width=10)
    cv2.imwrite('gray.png', gray_image)
    cv2.imwrite('bw_image.png', bw_image)
    cv2.imwrite('resized.png', resized)
    print_on_console_colored(image_resize(image, width=100))


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


def get_colored_text(text, color):
    if(color == 'red'): 
        return f"\033[31m{text}\033[0m"
    if(color == 'green'): 
        return f"\033[32m{text}\033[0m"
    if(color == 'blue'): 
        return f"\033[34m{text}\033[0m"

def print_on_console(list_2d):
    for row in list_2d:
        for pixel in row:
            print('*' if pixel > 128 else ' ', end=' ')
        print()

def print_on_console_colored(list_2d):
    for row in list_2d:
        for [r, g, b] in row:
            text = ''
            if(r < 128):
                text = get_colored_text('*', 'red')
            if(g < 128 and g < r):
                text = get_colored_text('*', 'green')
            if(b < 128 and b < g and b < r):
                text = get_colored_text('*', 'blue')

            print(text, end='  ')
        print()

main()

print(get_colored_text('hello', 'red') + get_colored_text('hii', 'green') + get_colored_text('blue', 'blue'))