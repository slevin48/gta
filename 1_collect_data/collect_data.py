import numpy as np
from grabscreen import grab_screen
import cv2
import time
import datetime
from getkeys import key_check
import os

z = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
q = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
zq = [0,0,0,0,1,0,0,0,0]
zd = [0,0,0,0,0,1,0,0,0]
sq = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

starting_value = 1

training_dataset = "training_data_2021-02-16-1"

while True:
    file_name = 'training_data/'+training_dataset+'/training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)
        
        break


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [Z, S, Q, D, ZQ, ZD, SQ, SD, NOKEY] boolean values.
    A replaced by Q for french keyboard
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if 'Z' in keys and 'Q' in keys:
        output = zq
    elif 'Z' in keys and 'D' in keys:
        output = zd
    elif 'S' in keys and 'Q' in keys:
        output = sq
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'Z' in keys:
        output = z
    elif 'S' in keys:
        output = s
    elif 'Q' in keys:
        output = q
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,40,960,560))
            last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            # screen = cv2.resize(screen, (480,270))
            # run a color convert:
            # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120))
            
            keys = key_check()
            output = keys_to_output(keys)
            # timing = datetime.datetime.now()
            training_data.append([screen,output])

            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
##            cv2.imshow('window',cv2.resize(screen,(640,360)))
##            if cv2.waitKey(25) & 0xFF == ord('q'):
##                cv2.destroyAllWindows()
##                break

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'training_data/'+training_dataset+'/training_data-{}.npy'.format(starting_value)

                    
        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


main(file_name, starting_value)
