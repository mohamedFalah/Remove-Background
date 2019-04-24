import cv2
import numpy as numpy

cap = cv2.VideoCapture(0)
panel = numpy.zeros([100,700,3], numpy.uint8)
cv2.namedWindow("panel")

def nothing(x):
    pass

cv2.createTrackbar("L - h", "panel",0,179, nothing)
cv2.createTrackbar("U - h", "panel", 179,179, nothing)

cv2.createTrackbar("L - s", "panel",0,255, nothing)
cv2.createTrackbar("U - s", "panel", 255,255, nothing)

cv2.createTrackbar("L - v", "panel",0,255, nothing)
cv2.createTrackbar("U - v", "panel", 255,255, nothing)

cv2.createTrackbar("S ROWS", "panel",0,720, nothing)
cv2.createTrackbar("E ROWS", "panel", 720,720, nothing)
cv2.createTrackbar("S COL", "panel",0,1280, nothing)
cv2.createTrackbar("E COL", "panel", 1280,1280, nothing)

while True: 
     _, frame = cap.read()
     s_r = cv2.getTrackbarPos("S ROWS", "panel") 
     e_r = cv2.getTrackbarPos("E ROWS", "panel") 
     s_c = cv2.getTrackbarPos("S COL", "panel") 
     e_c = cv2.getTrackbarPos("E COL", "panel") 
   
     roi = frame[s_r:e_r, s_c:e_c]
     hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

     l_h = cv2.getTrackbarPos("L - h", "panel") 
     u_h = cv2.getTrackbarPos("U - h", "panel") 
     l_s = cv2.getTrackbarPos("L - s", "panel") 
     u_s = cv2.getTrackbarPos("U - s", "panel") 
     l_v = cv2.getTrackbarPos("L - v", "panel")
     u_v = cv2.getTrackbarPos("U - v", "panel")  

     lower_green = numpy.array([l_h,l_s,l_v])
     upper_green = numpy.array([u_h,u_s,u_v])

     mask = cv2.inRange(hsv, lower_green, upper_green)
     mask_inv = cv2.bitwise_not(mask)

     bg = cv2.bitwise_and(roi, roi , mask=mask)
     fg = cv2.bitwise_and(roi, roi, mask=mask_inv) 
     bgS = cv2.resize(bg, (600, 600)) 
     fgS = cv2.resize(fg, (600, 600))                   

     cv2.imshow("bg", bgS)
     cv2.imshow("fg", fgS)

     cv2.imshow("panel", panel)
     k = cv2.waitKey(30) & 0xFF
     if k == 27:
         break

cap.release()
cv2.destroyAllWindows()
