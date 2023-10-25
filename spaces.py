import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# #BGR to Grayscale
gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# #BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# #BGR TO LAB/ L + a + b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#HSV TO BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
cv.imshow('HSV --> BGR', hsv_bgr)


# plt.imshow(rgb)
# plt.show()



cv.waitKey(0)