import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(gray)


cv2.imwrite("output.png", equalized)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Before Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("After Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.savefig("histogram_comparison.png")

plt.close()

print("Equalized image saved!")
print("Histogram comparison saved!")