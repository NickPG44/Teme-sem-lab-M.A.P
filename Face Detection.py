import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\Nick\OneDrive\Desktop\haarcascade_frontalface_default.xml')
img = cv2.imread(r'C:\Users\Nick\OneDrive\Desktop\fata.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)