import cv2

face_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in faces:
        cv2.

     

    
