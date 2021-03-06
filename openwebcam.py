# importeer benodigde library
import cv2

cap = cv2.VideoCapture(0)
# controleren of de webcam al open is
if not cap.isOpened():
    raise IOError("Kan de webcam niet openen")
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow("Input", frame)
    c = cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
