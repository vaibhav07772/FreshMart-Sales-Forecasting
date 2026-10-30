import cv2
import numpy as np

# IMAGE PATH DALNA MAT BHULNA
img1 = cv2.imread("practical9img1.png")
img2 = cv2.imread("practical9img2.png")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # cvtColor capital C
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 1 Face Detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

faces1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)

# Draw Rectangles
for (x, y, w, h) in faces2:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
print("Faces Detected in Image 2:", len(faces2))

# 2 Simple Face Recognition
def compare_faces(face1, face2):
    face1 = cv2.resize(face1, (100, 100))
    face2 = cv2.resize(face2, (100, 100)) # Yaha face2 tha
    hist1 = cv2.calcHist([face1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([face2], [0], None, [256], [0, 256])
    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return score

if len(faces1) > 0 and len(faces2) > 0:
    (x1, y1, w1, h1) = faces1[0]
    (x2, y2, w2, h2) = faces2[0]
    face1 = gray1[y1:y1+h1, x1:x1+w1]
    face2 = gray2[y2:y2+h2, x2:x2+w2]
    similarity = compare_faces(face1, face2)
    label = "Same Person" if similarity > 0.6 else "Different Person"
    cv2.putText(img2, label, (x2, y2-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

# 3. OBJECT DETECTION - Person detection via HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
boxes, _ = hog.detectMultiScale(gray2, winStride=(8, 8))
for (x, y, w, h) in boxes:
    cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)
print("Objects (people) detected:", len(boxes))

# 4. Show & Save
cv2.imshow("Result", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output.jpg", img2)