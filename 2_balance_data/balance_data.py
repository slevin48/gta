#  balance_data.py

import numpy as np
# import pandas as pd
# from collections import Counter
from random import shuffle
import os

training_dataset = "training_data_2021-02-16-1"

l = os.listdir("training_data/"+training_dataset)

# training_dataset = "training_data_2021-02-15-1"
# train_data = np.load("training_data/"+training_dataset+"/training_data-1.npy",allow_pickle=True)

train_data = np.load("training_data/"+training_dataset+"/"+l[0],allow_pickle=True)
for file in l[1:]:
    load_data = np.load("training_data/"+training_dataset+"/"+file,allow_pickle=True)
    train_data = np.concatenate((train_data,load_data))

print ("Train Data: ", train_data.shape)

# df = pd.DataFrame(train_data)
# print(df.head())
# print(Counter(df[1].apply(str)))

'''
Convert keys to a ...multi-hot... array
 0  1  2  3  4   5   6   7    8
[Z, S, Q, D, ZQ, ZD, SQ, SD, NOKEY] boolean values.
A replaced by Q for french keyboard
'''

shuffle(train_data)
z = []
s = []
q = []
d = []
zq = []
zd = []
sq = []
sd = []
nk = []

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0,0,0,0,0,0]:
        z.append([img,choice])
    elif choice == [0,1,0,0,0,0,0,0,0]:
        s.append([img,choice])
    elif choice == [0,0,1,0,0,0,0,0,0]:
        q.append([img,choice])
    elif choice == [0,0,0,1,0,0,0,0,0]:
        d.append([img,choice])
    if choice == [0,0,0,0,1,0,0,0,0]:
        zq.append([img,choice])
    elif choice == [0,0,0,0,0,1,0,0,0]:
        zd.append([img,choice])
    elif choice == [0,0,0,0,0,0,1,0,0]:
        sq.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,1,0]:
        sd.append([img,choice])
    elif choice == [0,0,0,0,0,0,0,0,1]:
        nk.append([img,choice])

# equilize everything
z = z[:len(zq)][:len(zd)]
# s ignored for training
# q = q[:len(z)] # ignored for training
# d = d[:len(z)] # ignored for training
zq = zq[:len(z)]
zd = zd[:len(z)]
# sq ignored
# sd ignored
# nk = nk[:len(z)] # ignored for training

final_data = z + zq + zd + nk
shuffle(final_data)

np.save("training_data/"+training_dataset+"-balanced.npy", final_data)