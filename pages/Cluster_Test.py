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
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array

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
for filename in glob.glob('Weather/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.convert('RGB')
    #img = np.array(im)
    #imgArr=img.reshape((img.shape[1]*img.shape[0],3))
    
    im = im.resize(newsize)
    image_list.append(im)

def image_feature(image_list):
    model = VGG16()
    model = Model(inputs = model.inputs, outputs = model.layers[-10].output)
    features = [];
    img_name = [];
    for i in range(len(image_list)):
        x = img_to_array(image_list[i])
        x=np.expand_dims(x,axis=0)
        x= preprocess_input(x)
        feat=model.predict(x)
        feat=feat.flatten()
        features.append(feat)
        img_name.append(i)
    return features,img_name

img_features,img_name = image_feature(image_list)
pca = PCA(n_components=10, random_state=22)
pca.fit(img_features)
x = pca.transform(img_features)
k = 5
clusters = KMeans(k, random_state = 22)
clusters.fit(x)
st.write(clusters.labels_)
image_cluster = pd.DataFrame(img_name,columns=['image'])
image_cluster["clusterid"] = clusters.labels_
row1, row2, row3, row4, row5, row6, row7 = 0,0,0,0,0,0,0
for i in range(len(image_cluster)):
    if image_cluster['clusterid'][i]==0:
        if row1 == 0:
            st.write("Cluster 1")
            row1+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==1:
        if row2 == 0:
            st.write("Cluster 2")
            row2+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==2:
        if row3 == 0:
            st.write("Cluster 3")
            row3+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==3:
        if row4 == 0:
            st.write("Cluster 4")
            row4+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==4:
        if row5 == 0:
            st.write("Cluster 5")
            row5+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==5:
        if row6 == 0:
            st.write("Cluster 6")
            row6+=1
        st.image(image_list[i])
    elif image_cluster['clusterid'][i]==6:
        if row7 == 0:
            st.write("Cluster 7")
            row7+=1
        st.image(image_list[i])
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

