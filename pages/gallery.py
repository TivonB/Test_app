import streamlit as st
from PIL import Image
import glob
                   


st.set_page_config(page_title="Gallery", layout="wide")
if 'start_index' not in st.session_state:
    st.session_state.start_index = 1
pic_list = []
#st.session_state.start_index = 1
#start_index = 1
with st.container():
    #image container
    st.write("---")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    def picDisplay(picResult):
        
        nextcol = 1
        newsize = (500,500)
        for i in range(len(picResult)):
            picture_result = picResult[i].resize(newsize)
            if(nextcol == 6):
                with col6:
                    st.image(picture_result)
                    nextcol = 1
            elif (nextcol == 5):
                with col5:
                    st.image(picture_result)
                    nextcol = 6
            elif (nextcol == 4):
                with col4:
                    st.image(picture_result)
                    nextcol = 5
            elif (nextcol == 3):
                with col3:
                    st.image(picture_result)
                    nextcol = 4
            elif (nextcol == 2):
                with col2:
                    st.image(picture_result)
                    nextcol = 3
            elif (nextcol == 1):
                with col1:
                    st.image(picture_result)
                    nextcol = 2
        return 0

image_list = []
newsize = (224,224)
for filename in glob.glob('Pic/*.png'): #assuming gif
    im=Image.open(filename)
    im = im.convert('RGB')
    #img = np.array(im)
    #imgArr=img.reshape((img.shape[1]*img.shape[0],3))
    
    im = im.resize(newsize)
    image_list.append(im)

def picGen(start_index, image_list):
    newsize = (200, 200)
    picTest_list = []
    for i in range(start_index,start_index+5):
        picTest_list.append(image_list[i])
    return picTest_list
with st.container():
    st.sidebar.subheader("CONTROLS")
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        weather_options = ['Rain','Snow','Sunny','Overcast','Night','Cloudy']
        weather = st.select_slider("Choose a Type of Weather",options = weather_options)
        st.write('The current weather is:',weather)
        if st.sidebar.button("Start Gallery"):
            picResult = picGen(1, image_list)
            picDisplay(picResult)
        if st.sidebar.button("Next Page") :
          st.session_state.start_index += 5
          #start_index += 12
          picResult = []
          picResult = picGen(st.session_state.start_index,image_list)
          picDisplay(picResult)
        if st.sidebar.button('Previous Page') :
          st.session_state.start_index -= 5
          #start_index = start_index - 12
          picResult = []
          picResult = picGen(st.session_state.start_index,image_list)
          picDisplay(picResult)

 


 
