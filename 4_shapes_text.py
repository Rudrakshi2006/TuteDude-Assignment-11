import cv2
import numpy as np

img=np.zeros((500,500,3),dtype=np.uint8)

cv2.line(img,(50,50),(450,50),(255,0,0),3)

pts=np.array([[100,100],[200,150],[150,250],[50,200]],np.int32)
cv2.polylines(img,[pts],True,(0,255,0),3)

cv2.putText(img,"OpenCV Practical",(80,450),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,(255,255,255),2)

cv2.imshow("Shapes",img)

cv2.waitKey(0)
cv2.destroyAllWindows()