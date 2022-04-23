# training_data.py
import numpy as np

def load_data(npfile):
    # npfile = "training_data.npy"
    training_data = np.load(npfile,allow_pickle=True) 
    img_array = []
    for i in range(len(training_data)):
        img_array.append(training_data[i][0])
    return img_array