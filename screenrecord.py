
import numpy as np
from PIL import ImageGrab
import cv2
import datetime
import time
import os


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name,allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main():

    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)


    paused = False
    while(True):

        if not paused:
            # 800x600 windowed mode
            screen =  np.array(ImageGrab.grab(bbox=(0,40,960,560)))
            timing = datetime.datetime.now()
            # screen = cv2.resize(screen, (160,120))
            training_data.append([screen,timing])

            
            if len(training_data) % 100 == 0:
                print(len(training_data))
                np.save(file_name,training_data)
                break
main()