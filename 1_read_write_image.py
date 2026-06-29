import cv2

img = cv2.imread(r"C:\Tutedude-Python\OpenCV_Practicals\image1.jpg")

if img is None:
    print("Image not loaded!")
    exit()

print("Image Shape:", img.shape)

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()