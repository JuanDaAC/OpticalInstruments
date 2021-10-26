import numpy as np
import cv2
import matplotlib.pyplot as plt

ejemplo = cv2.imread(r'C:\Users\User1\Pictures\Saved Pictures\patron.png',0)
fft_ejemplo = np.fft.fftshift(np.fft.fftn(ejemplo))
plt.imshow(np.log(np.abs(fft_ejemplo)))
plt.show()

# Este código hace una transformada de fourier a una imagen