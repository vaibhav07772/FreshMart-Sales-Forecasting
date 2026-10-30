import cv2
import numpy as np

img1 = cv2.imread("right.jpeg")
img2 = cv2.imread("left.jpeg")


gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(2000)
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matchers = bf.match(des1, des2)
matchers = sorted(matchers, key=lambda x: x.distance)

pts1 = np.float32([kp1[m.queryIdx].pt for m in matchers])
pts2 = np.float32([kp2[m.trainIdx].pt for m in matchers])


H, _ = cv2.findHomography(pts2, pts1, cv2.RANSAC)

h, w = img1.shape[:2]
result = cv2.warpPerspective(img2, H, (w*2, h))

overlay = result.copy()
overlay[0:h, 0:w] = img1
result = cv2.addWeighted(overlay, 0.5, result, 0.5, 0)

gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
coords = cv2.findNonZero(thresh)
x, y, w, z = cv2.boundingRect(coords)
result =  result[y:y+h, x:x+w]

cv2.imwrite("final_cleaning.jpg", result)
cv2.imshow("left", img1)
cv2.imshow("right", img2)
cv2.imshow("final Panorama", result)
cv2.waitKey(0)
cv2.destroyAllWindows()