# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:06:02 2022

@author: tivon_37vlsu0
"""

import streamlit as st
from PIL import Image
import random

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GANs Web Interface",layout="wide")

# ---- LOAD ASSETS ----
img = Image.open("Placeholder.png")

# ---- HEADER SECTION ----
with st.container():
    #st.subheader("This is the subheader.")
    st.title("Face-GANs.")
    #st.write("This is a test app")
    #st.write("This app is used to understand streamlit")
    
# ---- MAIN PAGE TOP ----
with st.container():
    st.write("---")
    st.image(img,use_column_width=True)
    
# ---- SIDE SLIDER ---- 
with st.container():
    st.write("---")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,10,10)
    synData = st.sidebar.slider("Synthetic Data",1,4000,4000)
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        st.sidebar.button("Generate GANs")
    with right_column:
        st.sidebar.button("Clear Input")
    st.write("---")
    st.subheader("Metrics")
    st.write(seedData , "real images")
    st.write(synData ,"synthetic images")
    st.write("---- GAN images")
    st.write("Generated in - minutes and - seconds")
        

        
        
# ---- MAIN PAGE BOTTOM ----
with st.container():
    st.write("---")
    #F_left_column, I_left_column, Mid_column, I_right_column, F_right_column = st.columns(5)
    #with F_left_column:
        #st.image(img)
    #with I_left_column:
        #st.image(img)
    #with Mid_column:
        #st.image(img)
    #with I_right_column:
        #st.image(img)
    #with F_right_column:
        #st.image(img)
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest = []
    k = random.sample(range(1,10), 6)
    for i in range(1,6):
        imgTest = Image.open(fileName+str(k[i])+fileTypeName)
        imgTest= imgTest.resize(newsize)
        picTest.append(imgTest)
    st.markdown(picTest)
        

    
        
