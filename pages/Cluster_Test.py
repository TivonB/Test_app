import streamlit as st
from PIL import Image
import glob

# for loading/processing the images  
import keras
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 
from keras.applications.vgg16 import preprocess_input 

# models 
from keras.applications.vgg16 import VGG16 
from keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# for everything else
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
                   


st.set_page_config(page_title="Cluster", layout="wide")
#image_list = []
#newsize = (200,200)
#for filename in glob.glob('Flowers/*.png'): #assuming gif
#    im=Image.open(filename)
#    im = im.resize(newsize)
#    image_list.append(im)
#st.image(image_list)

#count = 0
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
path = r"Flowers/"
# change the working directory to the path where the images are located
os.chdir(path)

# this list holds all the image filename
flowers = []
with os.scandir(path) as files:
  # loops through each file in the directory
    for file in files:
        if file.name.endswith('.png'):
          # adds only the image files to the flowers list
            flowers.append(file.name)
st.write(flowers)
