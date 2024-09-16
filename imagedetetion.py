import cv2
import numpy as np

vid = cv2.VideoCapture('http://192.168.1.253:8080/video')

while(vid.isOpened()):
    ret, frame = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))
    if not ret:
        continue
    '''img = cv2.line(frame, (0, 0), (width, height), (255, 130, 90), 10)
    img2 = cv2.line(img, (0, height), (width, 0), (255, 130, 90), 10)
    img3 = cv2.rectangle(img2, (100, 100), (250, 250), (0, 50, 200), 40)
    font = cv2.FONT_HERSHEY_SIMPLEX
    texto = cv2.putText(img3, 'Higiri', (2, 50), font, 2, (0, 30, 30), 5, cv2.LINE_AA)'''
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'): 
        break
    
vid.release()
cv2.destroyAllWindows()       


