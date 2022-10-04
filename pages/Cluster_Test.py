import streamlit as st
from PIL import Image
import glob

# for everything else
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import pandas as pd
import pickle

#---Kmeans Function ---
class KMean:
    def __init__(self,data,k,steps):
        self.data= data
        self.k = k
        self.steps = steps
        self.centers = np.array([self.data[i] for i in range(self.k)])
        self.colors = np.array(np.random.randint(0, 255, size =(self.k, 4)))/255
        self.colors[:,3]=1

    def distance(self,p1,p2):
        return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

    def initialize(self):
        """
            Initialize the Clusters.
        """
        self.clusters = {i: [] for i in range(self.k)}
        plt.scatter(self.centers[:, 0], self.centers[:, 1], s=200, color=self.colors)
        plt.scatter(self.data[:, 0], self.data[:,1],marker="*", s=100)
        plt.title("Initialize")
        plt.show()

    def fit(self):
        for step in range(self.steps):
            self.clusters = {i: [] for i in range(self.k)}

            for point in self.data:
                d= np.array([self.distance(point,c) for c in self.centers])
                c = np.argmin(d)
                self.clusters[c].append(point)

            self.clusters= {i:np.array(v) for i,v in self.clusters.items()}
            self.centers = np.array([self.clusters[i].mean(axis=0) for i in range(self.k)])
            self.visualize(step= step)

    def visualize(self,step):
        plt.title(f"Step : {step}")
        [plt.scatter(self.clusters[i][:, 0], self.clusters[i][:, 1], marker="*", s=100,
                    color = self.colors[i]) for i in range(self.k)]
        plt.scatter(self.centers[:, 0], self.centers[:, 1], s=200, color=self.colors)
        plt.show()

# --- Cluster Test ----
st.set_page_config(page_title="Cluster", layout="wide")
image_list = []
newsize = (224,224)
for filename in glob.glob('Flowers/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.convert('RGB')
    img=im.reshape((im.shape[1]*im.shape[0],3))
    #im = im.resize(newsize)
    #image_list.append(im)

#st.image(image_list)
st.write("ReShape: ", reshaped.shape)
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

