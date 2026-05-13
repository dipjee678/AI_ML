import streamlit as st 

st.title("Input your Information", anchor=False)

st.divider()

name = st.text_input("Enter your name", placeholder="Type your name...")

st.write("Your Name is:", name)

st.divider()

age = st.number_input("Enter your Age", min_value=0, step=1)

st.write("Your age is:", age)

st.divider()

pressed = st.button("Enter to confirm", type="primary")

if pressed:
    if name == "":
        st.error("Please enter your name")
    else:
        st.success(f"Your name is {name} and age is {age}")

selected = st.selectbox("Choose your profession",("Student","Employee","Businessman"),index=None,accept_new_options=True)


print(type(selected))

st.write(f"You selected {selected}")



