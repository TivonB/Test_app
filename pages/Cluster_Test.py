import streamlit as st
from PIL import Image
import glob

# for everything else
import numpy as np
from random import randint
import pandas as pd
import pickle
                   


st.set_page_config(page_title="Cluster", layout="wide")
image_list = []
newsize = (224,224)
for filename in glob.glob('Flowers/*.png'): #assuming gif
    im=Image.open(filename)
    #im = im.resize(newsize)
    image_list.append(im)

#st.image(image_list)
imgList = np.array(image_list[0])
st.write("Shape: ", imgList.shape)
imgList = np.array(image_list[0].resize(224,224))
st.write("ReShape: ", imgList.shape)
count = 0
#for img in image_list:  
#  temp_pixel = img.getpixel((0,0))
#  if type(temp_pixel) is tuple:
#       num = len(temp_pixel)
#  else:
#       num = 1
#  col, row = img.size
#  if num == 1:
#    value = 0
#    for x in range(col):
#      for y in range(row):
#        value+=int(img.getpixel((x,y)))
#    value /= (col*row)
#    st.write("Cluster: ", count) 
#    st.write("Value: ", value)
#  else:
#    Rvalue = 0
#    Gvalue = 0
#    Bvalue = 0
#    for x in range(col):
#      for y in range(row):
#        Rvalue+= int(img.getpixel((x,y))[0])
#        Gvalue+= int(img.getpixel((x,y))[1])
#        Bvalue+= int(img.getpixel((x,y))[2])
#    Rvalue /= (col*row)
#    Gvalue /= (col*row)
#    Bvalue /= (col*row)
#    st.write("Cluster: ", count) 
#    st.write("R Value: ", Rvalue)
#    st.write("G Value: ", Gvalue)
#    st.write("B Value: ", Bvalue)
#  count+=1

