# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 14:06:02 2022

@author: tivon_37vlsu0
"""

import streamlit as st
from PIL import Image
import random
import os
import streamlit.components.v1 as components


parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("st_clickable_images", path=build_dir)

picResult = []
#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GANs Web Interface",layout="wide")
def rando(gStop):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = ((200, 200))
    picTest = []
    k = random.sample(range(1,31), gStop)
    for i in range(1,gStop):
        imgTest = Image.open(fileName+str(k[i])+fileTypeName)
        imgTest= imgTest.resize(newsize)
        picTest.append(imgTest)
    return picTest

def clickable_images(paths, titles=[], div_style={}, img_style={}, key=None):
    """Display one or several images that can be clicked on".
    Parameters
    ----------
    paths: list
        The list of URLS of the images
    
    titles: list
        The (optional) titles of the images
    
    div_style: dict
        A dict with the CSS property/value pairs for the div container
    img_style: dict
        A dict with the CSS property/value pairs for the images
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    Returns
    -------
    int
        The index of the last image clicked on (or -1 before any click)
    """
    component_value = _component_func(
        paths=paths,
        titles=titles,
        div_style=div_style,
        img_style=img_style,
        key=key,
        default=-1,
    )

    return component_value


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
    if not picResult:
        st.write("no pic")
    else:
        clickable_images(picResult,titles=[f"Image #{str(i)}" for i in range(GANData)],div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},img_style={"margin": "5px", "height": "200px"},)
    #pick_img = st.selectbox("Which image?", 
           #[x for x in range(1, len(picResult))])

        

        
        
# ---- MAIN PAGE BOTTOM ----
#Change placeholder
    
        
