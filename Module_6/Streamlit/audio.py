import streamlit as st 

st.title("Input your files", anchor=False)
st.divider()


st.audio()


audio_file = st.file_uploader("Enter your image",type=['mp3','ogg','flac'],)



if audio_file:
    st.audio(audio_file)