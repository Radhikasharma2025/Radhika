import cv2

img = cv2.imread("input.jpg")
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imwrite("output.png", gaussian)

print("Gaussian filter applied successfully!")
print("Output saved as output.png")