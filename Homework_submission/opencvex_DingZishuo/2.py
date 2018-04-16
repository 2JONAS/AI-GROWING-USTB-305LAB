import cv2 as cv
import numpy as np

img = cv.imread('coin.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

circles1 = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 200, param1=150, param2=120)

circles = circles1[0, :, :]
circles = np.uint16(np.around(circles))
for i in circles[:]:
    cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)
    cv.circle(img, (i[0], i[1]), 2, (0, 255, 0), 10)
    cv.rectangle(img, (i[0]-i[2], i[1]+i[2]), (i[0]+i[2], i[1]-i[2]), (0, 0, 255), 5)
    print('圆心坐标：(', i[0], ',', i[1], ')')

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()