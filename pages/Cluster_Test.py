import streamlit as st
from PIL import Image
import glob
                   


st.set_page_config(page_title="Cluster", layout="wide")
image_list = []
for filename in glob.glob('Flowers/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.resize((200,200))
    image_list.append(im)
st.image(image_list)
