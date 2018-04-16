import cv2 as cv
import numpy as np

# 绿色HSV范围[35, 50, 50]~[77, 255, 255]
k1 = (77 - 35) / (10 - 0)
b1 = 77 - k1 * 10
k2 = (77 - 35) / (180 - 156)
b2 = 77 - k2 * 180


def red2green(pixel):
    x1 = pixel[0]
    if 0 <= x1 <= 10:
        y1 = k1 * x1 + b1
    elif 156 <= x1 <= 180:
        y1 = k2 * x1 + b2
    else:
        return pixel
    return [y1, pixel[1], pixel[2]]


img = cv.imread('strawberry.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
rows, cols, channels = img.shape

# 红色在HSV色域有两个范围
# (0-10)
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask0 = cv.inRange(hsv, lower_red, upper_red)

# (170-180)
lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask1 = cv.inRange(hsv, lower_red, upper_red)

# join my masks
mask = mask0+mask1

for i in range(rows):
    for j in range(cols):
        if mask[i, j] == 255:
            hsv[i, j] = red2green(hsv[i, j])

img = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('origin', img)

# ======================================================

bg = cv.imread('fruits.jpg')
# 缩小
berry = cv.resize(img, (int(cols * 0.3), int(rows * 0.3)))
# 放置坐标
y, x = 450, 450

# 划定ROI
rows, cols, _ = berry.shape
roi = bg[y:y + rows, x:x + cols]

img2gray = cv.cvtColor(berry, cv.COLOR_BGR2GRAY)
# 大于245（白色背景）变为0， 其余（草莓）变为白色
ret, mask = cv.threshold(img2gray, 245, 255, cv.THRESH_BINARY_INV)
mask_inv = cv.bitwise_not(mask)

# 放置草莓位置变黑
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv.bitwise_and(berry, berry, mask=mask)

dst = cv.add(img1_bg, img2_fg)
bg[y:y + rows, x:x + cols] = dst

cv.imshow('f', bg)
cv.waitKey(0)
cv.destroyAllWindows()