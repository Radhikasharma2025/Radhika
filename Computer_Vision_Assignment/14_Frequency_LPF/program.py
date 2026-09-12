import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

img_float = np.float32(img)

dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted = np.fft.fftshift(dft)

rows, cols = img.shape
crow = rows // 2
ccol = cols // 2

mask = np.zeros((rows, cols, 2), np.float32)

radius = 50

for y in range(rows):
    for x in range(cols):
        distance = ((y - crow) ** 2 + (x - ccol) ** 2) ** 0.5

        if distance < radius:
            mask[y, x] = 1

filtered = shifted * mask

filtered = np.fft.ifftshift(filtered)

result = cv2.idft(filtered)

result = cv2.magnitude(result[:, :, 0], result[:, :, 1])

result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX)
result = np.uint8(result)

cv2.imwrite("output.png", result)

print("Low Pass Filter applied successfully!")
print("Output saved as output.png")