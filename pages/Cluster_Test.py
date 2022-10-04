import streamlit as st
from PIL import Image
import glob

# for everything else
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import pandas as pd
import pickle

# for loading/processing the images  
#from keras.preprocessing.image import load_img
#from keras.preprocessing.image import img_to_array 
#from keras.applications.vgg16 import preprocess_input 

# models 
from keras.applications.vgg16 import VGG16 
from keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA



# --- Cluster Test ----
st.set_page_config(page_title="Cluster", layout="wide")
fileName = "Flowers/flower_"
fileTypeName = ".png"
image_list = []
newsize = (224,224)
#for filename in glob.glob('Flowers/*.png'): #assuming gif
for i in range(25):
    im=Image.open(fileName+str(i)+fileTypeName)
    im = im.convert('RGB')
    img = np.array(im)
    imgArr=img.reshape((img.shape[1]*img.shape[0],3))
    
    #im = im.resize(newsize)
    image_list.append(im)

st.write(image_list)
    
#st.image(image_list)
st.write("ReShape: ", imgArr.shape)
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

