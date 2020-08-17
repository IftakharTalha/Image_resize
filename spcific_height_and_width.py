import cv2

img = cv2.imread('test1.jpg')  
print('Original Dimensions : ', img.shape)  
  
width = 550  
height = 450  
dsize = (width, height)  
# resize image  
resized = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  