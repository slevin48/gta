import numpy as np

# training_data1 = np.load("training_data/training_data-1.npy",allow_pickle=True)

# data = []
# for i in range(500):
#     data.append(training_data1[i][1])

# import pandas as pd
# df = pd.DataFrame(data, columns = ['W', 'S', 'Q', 'D', 'WQ', 'WD', 'SQ', 'SD', 'NOKEY'])

# df.to_csv("training_data-1.csv")


import pandas as pd
import os

training_dataset = "training_data-2021-02-14-2"

l = os.listdir("training_data/"+training_dataset)
n = len(l)

os.mkdir("keyboard/"+training_dataset)

for k in range(n):
    training_data = np.load("training_data/"+training_dataset+"/training_data-"+str(k+1)+".npy",allow_pickle=True) 
    data
     = []

    for i in range(len(training_data)):
        
        data.append(training_data[i][1])

    df = pd.DataFrame(data, columns = ['Z', 'S', 'Q', 'D', 'ZQ', 'ZD', 'SQ', 'SD', 'NOKEY'])
    df.to_csv("keyboard/"+training_dataset+"/keyboard"+str(k+1)+".csv")