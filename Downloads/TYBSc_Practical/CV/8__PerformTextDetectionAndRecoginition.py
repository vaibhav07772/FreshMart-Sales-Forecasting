import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread(r"C:\Users\admin\Downloads\WhatsApp Image 2026-07-28 at 9.01.18 AM.jpeg")
image = cv2.resize(image, (600, 400))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
n_boxes = len(data['text'])
for i in range(n_boxes):
    if int(data['conf'][i]) > 60:
        x, y, w, h = (data['left'][i], data['top'][i],
                      data['width'][i], data['height'][i])
        text = data['text'][i]
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
cv2.imshow("Text Detection & Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()