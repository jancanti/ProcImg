import cv2
import numpy as np

img = cv2.imread('img/ingrid.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

cv2.imshow('', res)
cv2.waitKey(0)