import os
import cv2
import pywhatkit
import random
cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    no=random.random()
    ret,frame = cam.read()
    cv2.imshow("Capture",frame)
    if cv2.waitKey(1)==ord('s'):
        cv2.imwrite(f"Picture{no}"+".jpg",frame)
        pywhatkit.image_to_ascii_art(f"Picture{no}"+".jpg",f"Picture{no}"+".txt")
        s=f"Picture{no}"+".txt"
        os.startfile(f"G:\\Projects\\Camera_Capture_Device\\{s}")
    if cv2.waitKey(10)==ord('q'):
        break
#cam.release()
#cv2.destroyAllWindows()
