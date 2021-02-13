import cv2
import numpy as np
import glob
 
img_array = []
for i in range(500):
    filename = 'screenshots/training_data_'+str(i)+'.jpg'
    img = cv2.imread(filename)
    # height, width, layers = img.shape
    # size = (width,height)
    img_array.append(img)
 
size = (480, 270)

# out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'MP4V'), 10, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()