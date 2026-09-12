import cv2

img = cv2.imread("input.jpg")
mean = cv2.blur(img, (7, 7))

cv2.imwrite("output.png", mean)
