#Image

#pylint:disable=no-member

import cv2 as cv
import imutils
# img = cv.imread('33623_v9_bd.jpg')
# cv.imshow('Group of 5 people', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray People', gray)

# haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# print(f'Number of faces found = {len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# cv.imshow('Detected Faces', img)



# cv.waitKey(0)

#video

haar_cascade = cv.CascadeClassifier('haar_face.xml')

capture=cv.VideoCapture('IMG_6458.mp4')

while True:
    isTrue, frame = capture.read(0)
    frame = imutils.resize(frame, width=500)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #cv.imshow('Gray People', gray)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7,minSize=(30,30),flags=cv.CASCADE_SCALE_IMAGE)

    print(f'Number of faces found = {len(faces_rect)}')

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    cv.imshow('Detected Faces', frame)



    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()