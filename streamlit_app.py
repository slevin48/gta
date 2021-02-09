import streamlit as st
import numpy as np
import os
import cv2


@st.cache(show_spinner=False)
def load_image(dataset_id):
    training_data = np.load("training_data_angle/training_data-"+str(dataset_id)+".npy",allow_pickle=True)
    return training_data

st.sidebar.title("GTAV dataset")
dataset = st.sidebar.number_input("dataset",1,25)
images = load_image(dataset)
id = st.sidebar.slider("Frame",0,len(images)-1,0)
st.sidebar.markdown("## Steering angle:")
st.sidebar.write(images[id][1]) 

st.image(images[id][0],width=600)

video_file = open('project.avi', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
