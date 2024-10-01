from word_cloud import generate_word_cloud
import streamlit as st

st.title('Word Cloud Generator')

lang_choice = st.selectbox('Select language', ['english', 'french'])

text = st.text_area('Enter your text here')

if st.button('Generate Word Cloud'):
    cloud = generate_word_cloud(text, lang_choice)
    st.pyplot(cloud)