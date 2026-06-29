import cv2

img=cv2.imread("image1.jpg",0)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)

blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("Original",img)
cv2.imshow("Tophat",tophat)
cv2.imshow("Blackhat",blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()