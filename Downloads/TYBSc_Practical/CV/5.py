import cv2
import numpy as np
from rembg import remove

input_path = "modiji.jpg"
output_png = "rahul.png"


with open(input_path, "rb") as i:
    input_data = i.read()


output_data = remove(input_data)

with open(output_png, "wb") as o:
    o.write(output_data)
print("Background removed!")



person = cv2.imread(output_png, cv2.IMREAD_UNCHANGED)
background = cv2.imread("modiji.jpg")
if person is None or background is None:
    print("Error loading images")
    exit()


background = cv2.resize(background, (person.shape[1], person.shape[0]))

b, g, r, a = cv2.split(person)

alpha = a / 255.0

for c in range(3):
    background[:, :, c] = (
        alpha * person[:, :, c] + 
    (1 - alpha) * background[:, :, c]
    )

final = background.astype('uint8')


output_path = "modiji.jpg"
cv2.imwrite(output_path, final)
print("Final image saved at:", output_path)

cv2.imshow("final output", final)
cv2.waitKey(0)
cv2.destroyAllWindows()