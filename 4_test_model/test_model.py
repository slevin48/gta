# test_model.py

import numpy as np
from grabscreen import grab_screen
import cv2
import time
# from directkeys import PressKey,ReleaseKey, Z, Q, S, D
from directkeys2 import PressKey,ReleaseKey, Z, Q, S, D
from alexnet import alexnet
from getkeys import key_check

import random

training_dataset = "training_data_2021-02-16-1"

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'gta-{}-{}-{}-epochs-{}.model'.format(LR, 'alexnetv2',EPOCHS,training_dataset)        

t_time = 0.09

def straight():
##    if random.randrange(4) == 2:
##        ReleaseKey(Z)
##    else:
    PressKey(Z)
    ReleaseKey(Q)
    ReleaseKey(D)

def left():
    PressKey(Z)
    PressKey(Q)
    #ReleaseKey(Z)
    ReleaseKey(D)
    #ReleaseKey(Q)
    time.sleep(t_time)
    ReleaseKey(Q)

def right():
    PressKey(Z)
    PressKey(D)
    ReleaseKey(Q)
    #ReleaseKey(Z)
    #ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(D)
    
model = alexnet(WIDTH, HEIGHT, LR)
model.load("model/"+MODEL_NAME)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        
        if not paused:
            # 800x600 windowed mode
            #screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
            screen = grab_screen(region=(0,40,960,560))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120))

            prediction = model.predict([screen.reshape(160,120,1)])[0]
            print(prediction)

            turn_thresh = .75
            fwd_thresh = 0.70

            if prediction[0] > fwd_thresh:
                straight()
            elif prediction[5] > turn_thresh:
                left()
            elif prediction[6] > turn_thresh:
                right()
            else:
                straight()

        keys = key_check()
        print(keys)

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(Q)
                ReleaseKey(Z)
                ReleaseKey(D)
                time.sleep(1)

main()    