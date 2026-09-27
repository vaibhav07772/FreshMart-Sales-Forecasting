import cv2
import numpy as np

CHECKERBOARD =(7,7)

img = cv2.imread("chessboard3.jpg")

if img is None:
    print("hii TYDS")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)


if ret:
    criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.01)
    corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1, -1), criteria)


    cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
    cv2.imshow("Corners Detected", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("ho gaya surya bhai")

# import cv2
# import numpy as np

# CHECKERBOARD = (7, 6)

# img = cv2.imread("chessboard3.jpg")

# if img is None:
#     print("hii TYDS")
#     exit()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ret, corners = cv2.findChessboardCorners(
#     gray,
#     CHECKERBOARD,
#     cv2.CALIB_CB_ADAPTIVE_THRESH +
#     cv2.CALIB_CB_NORMALIZE_IMAGE +
#     cv2.CALIB_CB_FAST_CHECK
# )

# print("Corners Found =", ret)

# if ret:

#     criteria = (
#         cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
#         30,
#         0.001
#     )

#     corners2 = cv2.cornerSubPix(
#         gray,
#         corners,
#         (11, 11),
#         (-1, -1),
#         criteria
#     )

#     cv2.drawChessboardCorners(
#         img,
#         CHECKERBOARD,
#         corners2,
#         ret
#     )

#     cv2.imshow("Corners Detected", img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# else:
#     print("ho gaya surya bhai")