import numpy as np

training_data1 = np.load("training_data/training_data-1.npy",allow_pickle=True)

data = []
for i in range(500):
    data.append(training_data1[i][1])

import pandas as pd
df = pd.DataFrame(data, columns = ['W', 'S', 'Q', 'D', 'WQ', 'WD', 'SQ', 'SD', 'NOKEY'])

df.to_csv("training_data-1.csv")