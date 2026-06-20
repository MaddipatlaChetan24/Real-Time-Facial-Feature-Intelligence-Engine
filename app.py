import cv2

face_cascade = cv2.CascadeClassifier(haarcascade_frontalface_default.xml)

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)
    """
    detectMultiScale - scan and detect faces
    1.1 is the scale factor which controls how much the image size is reduced at each step.
    first try 100% then 2nd try 90% then so on... best is to use 1.1 balance,not too slow

    5 is the min Neigbours that means it will take 5 try / test cases to test wheather its real face or not 

    """

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        """
        x,y - top=left corner
        (x+w, y+h)
        face = [
        (100,150,80, 80) face1 
        (250,120, 90,90) face 2
        x - how far from left
        y - how far from top
        w - width of face
        h - height of face
        
        """

    cv2.imshow("Webcam Face Detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

