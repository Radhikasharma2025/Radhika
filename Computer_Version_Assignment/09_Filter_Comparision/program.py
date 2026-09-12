import cv2

img = cv2.imread("input.jpg")

mean = cv2.blur(img, (5, 5))

gaussian = cv2.GaussianBlur(img, (5, 5), 0)

median = cv2.medianBlur(img, 5)

cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)
