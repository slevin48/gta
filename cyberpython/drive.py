from PIL import ImageGrab,Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def pathing(minimap):
    lower = np.array([137-10, 139-10, 255])
    upper = np.array([137+10, 139+10, 255])

    hsv = cv2.cvtColor(minimap, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    matches = np.argwhere(mask==255)
    mean_y = np.mean(matches[:,1])
    target = minimap.shape[1]/2

    error = target - mean_y
    print(error)
    cv2.imshow("cv2screen", mask)
    cv2.waitKey(10)

# run for just 100 frames.
for i in range(100):
    minimap =  np.array(ImageGrab.grab(bbox=(44, 852, 44+278, 1050)))
    pathing(minimap)
    #screen = cv2.resize(screen, (960,540))
    #cv2.imshow("cv2screen", screen)
    #cv2.waitKey(10)
cv2.destroyAllWindows()