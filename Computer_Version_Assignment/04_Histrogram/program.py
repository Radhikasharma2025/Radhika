import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

histogram = cv2.calcHist([gray], [0], None, [256], [0, 256])

highest_intensity = histogram.argmax()

print("Intensity with highest frequency:", highest_intensity)

plt.plot(histogram)
plt.title("Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.savefig("output.png", bbox_inches="tight")

plt.close()
