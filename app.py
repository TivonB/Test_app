import streamlit as st

st.set_page_config(page_title="GANS", layout="wide")

#content of main_page

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        st.title("GANS DEMO ")

with st.container():
    
    st.markdown('##')

    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">A generative adversarial network (GAN) is a deep neural network that is trained with existing training data to generate new data of similar characteristics to the training data. For a GAN to work it needs two neural networks the generator, which is trained to produce fake data, and the discriminator, which is trained to distinguish the generator’s fake data from real examples. If the fake data generated is easily recognized as implausible by the discriminator, then the generator is penalized and must try again until it generates something plausible.  </p>', unsafe_allow_html=True)
    
