import cv2

# Open video (Replace with your video file or use 0 for webcam)
cap = cv2.VideoCapture(r"c:\Users\admin\Downloads\video_d02cfdd09c96.mp4")

# HOG Person Detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


# Create Tracker
def create_tracker():
    try:
        return cv2.TrackerKCF_create()
    except AttributeError:
        return cv2.legacy.TrackerKCF_create()


tracker = None
tracking = False

while True:
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.resize(frame, (680, 490))
    # Detect person if not tracking
    if not tracking:
        boxes, weights = hog.detectMultiScale(frame)

        for (x, y, w, h) in boxes:
            tracker = create_tracker()
            tracker.init(frame, (x, y, w, h))
            tracking = True
            break

    # Track detected person
    else:
        success, box = tracker.update(frame)

        if success:
            x, y, w, h = map(int, box)

            cv2.rectangle(frame,
                          (x, y),
                          (x + w, y + h),
                          (0, 255, 0),
                          2)

            cv2.putText(frame,
                        "Tracking",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2)
        else:
            tracking = False

    cv2.imshow("Object Detection & Tracking", frame)

    if cv2.waitKey(30) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()