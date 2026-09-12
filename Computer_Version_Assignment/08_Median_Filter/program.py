import cv2

img = cv2.imread("input.jpg")

median = cv2.medianBlur(img, 5)

cv2.imwrite("output.png", median)

print("Median filter applied successfully!")
print("Output saved as output.png")