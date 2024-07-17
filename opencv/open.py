import  cv2

haar_cas=cv2.CascadeClassifier('Object-oriented Programming in 7 minutes _ Mosh.mp4')
image =cv2.imread('pic.jpeg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = haar_cas.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)
     
cv2.imshow("Gray",image)
cv2.waitKey()