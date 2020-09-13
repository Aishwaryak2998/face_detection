import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\aishw\\OneDrive\\Desktop\\urgh\\face_detection\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)  #opens webcam

while cap.isOpened():           #each frame of the video is converted to gray. rgb to gray
    _, img =  cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1, 4 )

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Works")
        break

cap.release()
cv2.destroyAllWindows