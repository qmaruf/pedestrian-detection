import config
import json
import cv2
import numpy as np
import time

def run(cap, polygon_points):
    polygon_points = np.array([[point['X'], point['Y']] for point in polygon_points ]).reshape((-1, 1, 2))
    
    _, frame1 = cap.read()
    while(cap.isOpened()):        
        _, frame2 = cap.read()
        frame2orig = frame2.copy()        
        
        frame1gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        frame2gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        framediff = cv2.absdiff(frame2gray, frame1gray)
        _, framediff = cv2.threshold(framediff, 30, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3, 3), np.uint8)
        framediff = cv2.dilate(framediff, kernel, iterations=1)
        
        contours, hierarchy = cv2.findContours(framediff.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        valid = []        
        
        for cnt in contours:            
            if cv2.contourArea(cnt) > 10:
                M = cv2.moments(cnt)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                                
                inside = cv2.pointPolygonTest(polygon_points, (cX, cY), False)     
                if inside < 0:
                    frame2 = cv2.circle(frame2, (cX, cY), 2, (0, 0, 255), 5)
                else:
                    frame2 = cv2.circle(frame2, (cX, cY), 2, (0, 255, 0), 5)

        cv2.polylines(frame2,[polygon_points],True,(0,255,255))
        cv2.imshow('frame', frame2)        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        frame1 = frame2orig        
        time.sleep(0.05)   
        
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    with open(config.VIDEO_POLYGON_PATH) as hndl:
        polygon_points = json.load(hndl)
    cap = cv2.VideoCapture(config.VIDEO_PATH)
    
    run(cap, polygon_points)