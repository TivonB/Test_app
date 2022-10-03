import streamlit as st
from PIL import Image
import glob
                   


st.set_page_config(page_title="Cluster", layout="wide")
image_list = []
newsize = (200,200)
for filename in glob.glob('Flowers/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.resize(newsize)
    image_list.append(im)
st.image(image_list)

col, row = im.size
count = 0
for img in im:
  Rvalue = 0
  Gvalue = 0
  Bvalue = 0
  for x in range(col):
    for y in range(row):
      Rvalue+= int(img.getpixel((x,y))[0])
      Gvalue+= int(img.getpixel((x,y))[1])
      Bvalue+= int(img.getpixel((x,y))[2])
  Rvalue /= (col*row)
  Gvalue /= (col*row)
  Bvalue /= (col*row)
  st.write("Cluster: ", count) 
  st.write("R Value: ", Rvalue)
  st.write("G Value: ", Gvalue)
  st.write("B Value: ", Bvalue)
  count+=1
