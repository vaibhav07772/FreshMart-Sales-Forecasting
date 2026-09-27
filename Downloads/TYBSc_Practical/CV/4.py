import cv2
import numpy as np
import os

img = "car1.jpeg"

if not os.path.exists(img):
    print("hey bhagwan")
    exit()


gray_image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
if gray_image is None:
    print("la la la")
    exit()

colorized_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

cv2.imshow("Original image", gray_image)
cv2.imshow("Colorized image", colorized_image)

output_path = "car1.jpeg"
cv2.imwrite(output_path, colorized_image)
print("colorized_image", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()