import cv2

image = cv2.imread('nishant.png')
height, width, channels = image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
(thresh, bw_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

cv2.imwrite('gray.png', gray_image)
cv2.imwrite('bw_image.png', bw_image)
print({'height': height, 'width': width})