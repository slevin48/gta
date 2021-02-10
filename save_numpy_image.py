# save_numpy_image
# https://theailearner.com/2018/10/15/creating-video-from-images-using-opencv-python/

import numpy as np
training_data = np.load("training_data/training_data-5.npy",allow_pickle=True)
import cv2
 

img_array = []

for i in range(len(training_data)):
    # print(img[0][0])
    img_array.append(training_data[i][0])
    cv2.imwrite("screenshots/training_data_"+str(i)+".jpg",training_data[i][0])