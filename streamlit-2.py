import streamlit as st

st.title('Lesson 01.02: Intro to Layouts and Images')


st.sidebar.image("https://static.streamlit.io/examples/cat.jpg", width=100)
st.sidebar.header("Options")
text = st.sidebar.text_area("Paste text here")

button1 = st.sidebar.button("Clean Text")
if button1:
    col1, col2 = st.columns(2)
    col1_expander = col1.expander("Expand Original Text")
    with col1_expander:
        col1_expander.write(text)

    col2_expander = col2.expander("Expand Cleaned Text")
    with col2_expander:
        col2_expander.write(text.lower())