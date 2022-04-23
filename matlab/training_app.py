import streamlit as st
import numpy as np
import os
import cv2


@st.cache(show_spinner=False)
def load_image():
    training_data = np.load("training_data/training_data-0.npy",allow_pickle=True)
    return training_data

st.sidebar.title("GTAV dataset")
images = load_image()
id = st.sidebar.slider("Frame",0,len(images)-1,0)
st.sidebar.markdown("## Recorded time:")
st.sidebar.write(images[id][1]) 

st.image(images[id][0],width=600)
