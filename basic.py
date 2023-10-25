import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

#Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blurring a image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#EDGE CASCADE
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny', canny)


#Dilatting the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

#Eroding the image
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded', eroded)

#Resize the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#Cropping the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)