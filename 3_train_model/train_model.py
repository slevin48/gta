# train_model.py

import numpy as np
from alexnet import alexnet

training_dataset = "training_data_2021-02-16-1"

WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'gta-{}-{}-{}-epochs-{}.model'.format(LR, 'alexnetv2',EPOCHS,training_dataset)        

model = alexnet(WIDTH, HEIGHT, LR)

for i in range(EPOCHS):
    
    train_data = np.load("training_data/"+training_dataset+"-balanced.npy",allow_pickle=True)

    train = train_data[:-100]
    test = train_data[-100:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

    model.save("model/"+MODEL_NAME)


# tensorboard --logdir=foo:D:\devel\gta\log
