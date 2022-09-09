# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:06:02 2022

@author: tivon_37vlsu0
"""

import streamlit as st
from PIL import Image

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:",layout="wide")

# ---- LOAD ASSETS ----
img = Image.open("domo1.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("This is the subheader.")
    st.title("This the Title location")
    st.write("This is a test app")
    st.write("This app is used to understand streamlit")
    
# ---- MORE INFO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Further Left Testing")
        st.write("##")
        st.write("This is testing of the left column")
    with right_column:
        st.header("Further Right Testing")
        st.write("##")
        st.write("This is testing of the right column")
        
# ---- IMAGE ----
with st.container():
    st.write("---")
    image_column, text_column = st.columns(2)
    with image_column:
        st.header("Further Image Testing")
        st.image(img)
    with text_column:
        st.header("Further Image Text Testing")
        st.write("##")
        st.write("This is testing of the Image Text column")
        
# ---- SLIDER ---- 
with st.container():
    st.write("---")
    st.slider("Slider tester", 1, 5000, 2000)
    st.sidebar.multiselect(
            "Control which features?"
        )
    
        
