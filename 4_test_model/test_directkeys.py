from directkeys2 import PressKey,ReleaseKey, Z, Q, S, D
from getkeys import key_check
import time

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
    ReleaseKey(Q)

def right():
    PressKey(Z)
    PressKey(D)
    ReleaseKey(Q)
    #ReleaseKey(Z)
    #ReleaseKey(D)
    ReleaseKey(D)

def main():
    
    paused = False
    while(True):
        
        if not paused:
                
            straight()
            print(key_check())
            time.sleep(1)
            left()        
            print(key_check())
            time.sleep(1)
            right()
            print(key_check())
            time.sleep(1)

        # keys = key_check()
main()    