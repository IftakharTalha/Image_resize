import cv2
img = cv2.imread('test1.jpg')  
  
print('Original Dimensions : ', img.shape)  
  
scale = 160  
width = int(img.shape[1] * scale / 100)  
height = int(img.shape[0] * scale / 100)  

dsize = (width, height)  


resized = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)  
  
print('Resized Dimensions : ', resized.shape)  
  
cv2.imshow("Resized image", resized)  
cv2.waitKey(0)  
cv2.destroyAllWindows() 