# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:06:02 2022

@author: tivon_37vlsu0
"""

import streamlit as st
from PIL import Image
import random

picResult = 0
#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GANs Web Interface",layout="wide")
def rando(gStop):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest = []
    k = random.sample(range(1,31), gStop)
    for i in range(1,gStop):
        imgTest = Image.open(fileName+str(k[i])+fileTypeName)
        #imgTest= imgTest.resize(newsize)
        picTest.append(imgTest)
    return picTest

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
    st.subheader("Metrics")
    st.write(seedData , "real images")
    st.write(synData ,"synthetic images")
    GANData = seedData*synData
    st.write(GANData,"GAN images")
    st.write("Generated in - minutes and - seconds")
    
with st.container():
    st.write("---")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,5,5)
    synData = st.sidebar.slider("Synthetic Data",1,5,5)
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        if st.sidebar.button("Generate GANs"):
            picResult = rando(GANSData)
    with right_column:
        st.sidebar.button("Clear Input")

with st.container():
    st.write("---")
    if len(picResult) > 0:
        st.image(picResult, width = 200)
    else:
        st.write("no pic")
        

        
        
# ---- MAIN PAGE BOTTOM ----
#Change placeholder
    
        
