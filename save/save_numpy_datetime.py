import numpy as np
import cv2
import os
import pandas as pd

training_dataset = "training_data-2021-02-12-4"

l = os.listdir("training_data/"+training_dataset)
n = len(l)

os.mkdir("timeline/"+training_dataset)

for k in range(n):
    training_data = np.load("training_data/"+training_dataset+"/training_data-"+str(k+1)+".npy",allow_pickle=True) 
    time_array = []

    for i in range(len(training_data)):
        
        time_array.append(training_data[i][1])

    df = pd.DataFrame(time_array,columns=["time"])
    df.to_csv("timeline/"+training_dataset+"/timeline"+str(k+1)+".csv")