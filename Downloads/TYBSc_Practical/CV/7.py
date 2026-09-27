import cv2
import numpy as np

img1 = cv2.imread(r"C:\Users\admin\OneDrive\TYDS_surya_the_hero\WhatsApp Image 2026-07-14 at 7.47.50 AM (1).jpeg")
img2 = cv2.imread(r"C:\Users\admin\OneDrive\TYDS_surya_the_hero\WhatsApp Image 2026-07-14 at 7.47.50 AM.jpeg")

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

matchesMask = mask.ravel().tolist()
draw_params = dict(matchColor=(0, 255, 0),       # Draw inliers in green
                   singlePointColor=None,
                   matchesMask=matchesMask,      # Specify inliers to draw
                   flags=2)                      # cv2.DrawMatchesFlags_DEFAULT
result = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, **draw_params)
result = cv2.resize(result, (800, 900))

cv2.imshow("RANSAC Feature Matching", result)
cv2.waitKey(0)
cv2.destroyAllWindows()