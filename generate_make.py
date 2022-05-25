import cv2
import numpy as np


origin_img = cv2.imread('1.jpg')
img_size = 256
origin_img = cv2.resize(origin_img, (img_size, img_size))

mask = np.ones((img_size, img_size)) * (origin_img[:, :, 0] > 220) * 255

kernel = np.ones((3, 3), np.uint8)
img_dilate = cv2.dilate(mask, kernel, iterations=2)
# origin_img[origin_img[:, :, 0] > 220]=0

# cv2.imshow('a',img_dilate)
# cv2.imshow('origin',mask)
# cv2.waitKey(0)
cv2.imwrite('mask_2.png', mask)
