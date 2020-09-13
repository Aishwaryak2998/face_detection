import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\aishw\\OneDrive\\Desktop\\urgh\\face_detection\\haarcascade_frontalface_default.xml")

img = cv2.imread("C:\\Users\\aishw\\OneDrive\\Desktop\\urgh\\face_detection\\j.jpg")  #any image you want to try
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #convert the colored image to gray
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05,minNeighbors=5 )
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)  
resized = cv2.resize(img, (int(img.shape[1]), int(img.shape[0])))  

cv2.imshow("Gray", resized)
cv2.waitKey(0) 