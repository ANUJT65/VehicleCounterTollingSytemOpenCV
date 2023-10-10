import cv2
import numpy as np
import flet as ft





cap =cv2.VideoCapture('video.mp4')

min_width_react=80
min_height_react=80

#initialise substructor

    
algo =cv2.bgsegm.createBackgroundSubtractorMOG()
count_line_position =600

def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx = x+x1
    cy= y+y1
    return cx,cy
detect=[]
offset=7 #pixelerror
counter=0
    

while True:
    ret,frame1= cap.read()
    grey =cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur =cv2.GaussianBlur(grey,(3,3),5)
    #applying on frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatada= cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernal)
    dilatada= cv2.morphologyEx(dilatada,cv2.MORPH_CLOSE,kernal)
    counterSahpe,h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.line(frame1,(150,count_line_position),(600,count_line_position),(255,127,0),4)

    for (i,c) in enumerate(counterSahpe):
        (x,y,w,h)=cv2.boundingRect(c)
        Validate_counter= (w>= min_width_react) and (h>= min_height_react)
        if not Validate_counter:
            continue
        center = center_handle(x, y, w, h)
        if center[0] < frame1.shape[1] / 2:
             cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
             detect.append(center)
             cv2.circle(frame1, center, 4, (0, 0, 255), -1)
          

        #cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        #center = center_handle(x,y,w,h)
        #detect.append(center)
        #cv2.circle(frame1,center,4,(0,0,255),-1)


        for(x,y) in detect:
            if y<(count_line_position+offset) and y>(count_line_position-offset):
                counter+=1
            cv2.line(frame1,(150,count_line_position),(600,count_line_position),(0,255,255),4)
            detect.remove((x,y))
            print("Vehicle counter:"+str(counter))


    cv2.putText(frame1,"VEHICLE COUNTER:"+str(counter),(150,70),cv2.FONT_HERSHEY_SIMPLEX,2,(300,0,0),5)





         






    cv2.imshow('Detector',dilatada)







    cv2.imshow('Video Original',frame1)
    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
