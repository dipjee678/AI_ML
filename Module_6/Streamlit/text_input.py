import streamlit as st 

st.title("My frist Streamlit Web Apps", anchor=False,)


st.header("Content 1",divider=True)

st.subheader("Content 1 Subheader")

st.write("Hello Dip")

st.text("Hello World")

st.markdown(":red[**Hello**] *World*")

st.markdown(":red-background[:orange[**Hello**] *World*]")


a=10
b=20

st.write(a,b)
