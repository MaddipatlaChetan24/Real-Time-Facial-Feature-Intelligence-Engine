import cv2

face_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("/Users/chetan/Documents/face emotion dection/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

cv2.destroyAllWindows()

     

    
