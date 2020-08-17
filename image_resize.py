import cv2

img = cv2.imread("test1.jpg")

scale = 60

print("original Dimensions:",img.shape)

width = int(img.shape[1]*scale/100)
height = int(img.shape[0]*scale/100)

dsize = (height, width)

resize = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)

print("Resized Dimensions:",resize.shape)

cv2.imshow("Resized Image",resize)
cv2.waitKey(0)
cv2.destroyAllWindows()