import cv2
import numpy as np

img = cv2.imread("input.jpg", 0)

img_float = np.float32(img)

dft = cv2.dft(img_float, flags=cv2.DFT_COMPLEX_OUTPUT)

shifted = np.fft.fftshift(dft)

magnitude = cv2.magnitude(
    shifted[:, :, 0],
    shifted[:, :, 1]
)
magnitude = np.log(magnitude + 1)

magnitude = cv2.normalize(
    magnitude,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)

magnitude = np.uint8(magnitude)

cv2.imwrite("output.png", magnitude)
