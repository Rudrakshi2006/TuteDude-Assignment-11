import cv2

img = cv2.imread(r"C:\Tutedude-Python\OpenCV_Practicals\image1.jpg")

# Create resizable windows
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Resized", cv2.WINDOW_NORMAL)

# Set window sizes
cv2.resizeWindow("Original", 500, 500)
cv2.resizeWindow("Resized", 500, 500)

resized = cv2.resize(img, (400, 300))

cv2.imshow("Original", img)
cv2.imshow("Resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()