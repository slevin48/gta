import streamlit as st
import numpy as np
import os
import cv2


@st.cache(show_spinner=False)
def load_image(training_dataset,dataset_id):
    training_data = np.load("training_data/"+training_dataset+"/training_data-"+str(dataset_id)+".npy",allow_pickle=True)

    return training_data

st.sidebar.title("GTAV dataset")
datastore = st.sidebar.text_input("datastore","training_data_2022-04-24-1")
dataset = st.sidebar.number_input("dataset",1,25)
images = load_image(datastore,dataset)
id = st.sidebar.slider("Frame",0,len(images)-1,0)
st.sidebar.markdown("## Controller Input:")
st.sidebar.write(images[id][1]) 

st.title("Simulated road data")

st.image(images[id][0],width=600)

# video_file = open('project.mp4', 'rb')
# video_bytes = video_file.read()
# st.video(video_bytes)
