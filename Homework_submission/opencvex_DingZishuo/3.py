import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('bottle.jpg')
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 200)

plt.subplot(121), plt.imshow(rgb)
plt.title('Origin'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge'), plt.xticks([]), plt.yticks([])

plt.show()
