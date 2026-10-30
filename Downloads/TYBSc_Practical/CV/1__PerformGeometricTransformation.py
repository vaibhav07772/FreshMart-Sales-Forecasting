import cv2
import numpy as np

img = cv2.imread("earth.jpg")
if img is None:
    print("hii vaibhav")
    exit()

rows, cols = img.shape[:2]

T = np.float32([[1, 0, 100],
                [0, 1, 50]])

translate = cv2.warpAffine(img, T, (cols, rows))

R = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
roatated = cv2.warpAffine(img, R, (cols, rows))

scaled = cv2.resize(img, None, fx=0.6, fy=0.8)

cv2.imshow("o_img", img)
cv2.imshow("T_img", translate)
cv2.imshow("R_img", roatated)
cv2.imshow("scaled", scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()