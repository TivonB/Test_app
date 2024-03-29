# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:06:02 2022

@author: tivon_37vlsu0
"""

import streamlit as st
from PIL import Image
import random

picResult = []
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
    resized_image = img.resize((336, 336))
    st.image(resized_image)
    
# ---- SIDE SLIDER ---- 
with st.container():
    st.write("---")
    #st.slider("Slider tester", 1, 5000, 2000)
    seedData = st.sidebar.slider("Seed Data",1,5,5)
    synData = st.sidebar.slider("Synthetic Data",1,5,5)
    GANData = seedData*synData
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        if st.sidebar.button("Generate GANs"):
            picResult = rando(GANData)
    with right_column:
        if st.sidebar.button("Clear Input"):
            picResult = []
    st.write("---")
    st.subheader("Metrics")
    st.write(seedData , "real images")
    st.write(synData ,"synthetic images")
    st.write(GANData,"GAN images")
    st.write("Generated in - minutes and - seconds")
        
    

with st.container():
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    if not picResult:
        st.write("")
    else:
        nextcol = 1
        newsize = (500, 500)
        for i in range(len(picResult)):
            imgRe= picResult[i].resize(newsize)
            if (nextcol == 6):
                with col6:
                    st.image(imgRe,caption="Pic/Test_"+str(i))
                    nextcol = 1
            elif (nextcol == 5):
                with col5:
                    st.image(imgRe,caption="Pic/Test_"+str(i))
                    nextcol = 6
            elif (nextcol == 4):
                with col4:
                    st.image(imgRe,caption="Pic/Test_"+str(i))
                    nextcol = 5
            elif (nextcol == 3):
                with col3:
                    st.image(imgRe,caption="Pic/Test_"+str(i))
                    nextcol = 4
            elif (nextcol == 2):
                with col2:
                    st.image(imgRe,caption="Pic/Test_"+str(i))
                    nextcol = 3
            elif (nextcol == 1):
                with col1:
                    st.image(imgRe,caption="Test_"+str(i))
                    nextcol = 2
            
            
                
            
    #pick_img = st.selectbox("Which image?", 
           #[x for x in range(1, len(picResult))])

        

        
        
# ---- MAIN PAGE BOTTOM ----
#Change placeholder
    
        
