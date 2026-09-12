import cv2
import numpy as np

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
min_value = np.min(gray)
max_value = np.max(gray)

print("Minimum intensity:", min_value)
print("Maximum intensity:", max_value)
gray = gray.astype(float)
stretched = (gray - min_value) * 255 / (max_value - min_value)
stretched = stretched.astype(np.uint8)
cv2.imwrite("output.png", stretched)
