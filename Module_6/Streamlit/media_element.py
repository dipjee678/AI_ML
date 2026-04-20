import streamlit as st 

st.title("Input your files", anchor=False)
st.divider()

images = st.file_uploader("Enter your image (at max 2)",type=['jpg','jpeg','png'],accept_multiple_files=True)


print(type(images))



if images:
    if (len (images)>2):
        st.warning("You uploaded 3 photos")
    col = st.columns(len(images))

    for i,per_image in enumerate(images):
        with col[i]:
            st.image(per_image)


st.image("https://cdn.pixabay.com/photo/2015/04/19/08/32/flower-729510_1280.jpg")