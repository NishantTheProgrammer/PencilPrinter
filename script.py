import cv2

import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

def main():
    image = cv2.imread('nishant.png')
    height, width, channels = image.shape
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    resized = image_resize(bw_image, width=15)
    cv2.imwrite('gray.png', gray_image)
    cv2.imwrite('bw_image.png', bw_image)
    cv2.imwrite('resized.png', resized)
    print(resized)


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

main()
