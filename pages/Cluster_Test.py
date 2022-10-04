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
image_list = []
newsize = (224,224)
for filename in glob.glob('Flowers/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.convert('RGB')
    img = np.array(im)
    imgArr=img.reshape((img.shape[1]*img.shape[0],3))
    
    #im = im.resize(newsize)
    image_list.append(im)

model = VGG16()
# remove the output layer
model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

def extract_features(file, model):
    # load the image as a 224x224 array
    img = image.open(file)
    # convert from 'PIL.Image.Image' to numpy array
    img = np.array(img) 
    # reshape the data for the model reshape(num_of_samples, dim 1, dim 2, channels)
    #reshaped_img = img.reshape(1,224,224,3) 
    # prepare image for model
    #imgx = preprocess_input(reshaped_img)
    # get the feature vector
    features = model.predict(img, use_multiprocessing=True)
    return features

for flower in image_list:
    # try to extract the features and update the dictionary
    feat = extract_features(flower,model)
    data[flower] = feat

filenames = np.array(list(data.keys()))

# get a list of just the features
feat = np.array(list(data.values()))
st.write(feat.shape)

#st.image(image_list)
#st.write("ReShape: ", imgArr.shape)
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

