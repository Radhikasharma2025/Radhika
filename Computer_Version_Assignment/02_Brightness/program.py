import cv2


img = cv2.imread("input.jpg")
brightness = 50

bright = cv2.add(img, brightness)

cv2.imwrite("output.png", bright)