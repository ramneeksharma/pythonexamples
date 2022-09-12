from calendar import c
import cv2 as cv

A = cv.imread(cv.samples.findFile("starry_night.jpg"), cv.IMREAD_COLOR)
print(type(A))

B = cv.Mat(shape = (2,2), dtype = cv.CV_8UC3, strides = (0,0,255));
print(type(B))
print(B)
