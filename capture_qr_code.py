import cv2
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
while True:
    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if data:
        a=data
        break
    cv2.imshow("QRCODEscanner", img)    
    if cv2.waitKey(1) == ord("q"):
        break
print(str(a))
cap.release()
cv2.destroyAllWindows()
