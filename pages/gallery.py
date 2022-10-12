import streamlit as st
from PIL import Image

                   


st.set_page_config(page_title="Gallery", layout="wide")
#if 'start_index' not in st.session_state:
    #st.session_state.start_index = 1
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
                   

def picGen(start,end):
    fileName = "Pic/Test_"
    fileTypeName = ".png"
    newsize = (200, 200)
    picTest_list = []
    for i in range(start,end):
        pic_test = Image.open(fileName+str(i)+fileTypeName)
        pic_test = pic_test.resize(newsize)
        picTest_list.append(pic_test)
    return picTest_list
with st.container():
    start = 0
    end = 12
    st.sidebar.subheader("CONTROLS")
    left_column, right_column = st.sidebar.columns(2)
    with left_column:
        weather_options = ['Rain','Snow','Sunny','Overcast','Night','Cloudy']
        weather = st.select_slider("Choose a Type of Weather",options = weather_options)
        st.write('The current weather is:',weather)
        if st.sidebar.button("Start Gallery"):
            picResult = picGen(start,end)
            picDisplay(picResult)
        if st.sidebar.button("Next Page") :
          start += 12
          end += 12
          #start_index += 12
          picResult = []
          picResult = picGen(start,end)
          picDisplay(picResult)
        if st.sidebar.button('Previous Page') :
          start -= 12
          end -= 12
          #start_index = start_index - 12
          picResult = []
          picResult = picGen(start,end)
          picDisplay(picResult)

 
