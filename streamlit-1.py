import streamlit as st

st.title('Streamlit App')

st.write('This is my new Streamlit app!')

st.header('Start of the Checkbox Section')
like = st.checkbox('Do you like this app?')   

button2 = st.button('Submit')
if button2:
    if like:
        st.write('Thank you!, I know cuz I am awesome! :)')
    else:
        st.write('You are son of a gun! :(')


st.header("Strat of the Radio Button Section")
animal = st.radio("What animal is your favorite?", ("Lions", "Tiger", "Bears"))
button3 = st.button("Submit an Animal")
if button3: 
    if animal == "Lions":
        st.write("ROAR!")
    if animal == "Tiger":
        st.write("Shut the fuck up!")

st.header("Strat of the Selectbox Button Section")
animal = st.selectbox("What animal is your favorite?", ("Lions", "Tiger", "Bears"))
button4 = st.button("Submit Animal")
if button4: 
    if animal == "Lions":
        st.write("ROAR!")
    if animal == "Tiger":
        st.write("Shut up!")



st.header("Strat of the Multiselect Section")
options = st.multiselect("What animals do you like", ("Lion", "Tiger", "Bear"))
button5 = st.button("Print Animals")
if button5: 
    st.write(options)


st.header("Start of the Slider Section")
epochs_num = st.slider("How many epochs?", min_value=1, max_value=100, step=1, value=3)
if st.button("Slider Button"):
    st.write(epochs_num)
    if type(epochs_num) == int:
        st.write(f"{epochs_num} is integer")


st.header("Start of the Text Input Section")

usr_text = st.text_input("What is your favorite movie?")
if st.button("Text button"):
    st.write(f"The user like: {usr_text}")

usr_num = st.number_input("What is your favorite number?")
if st.button("Number button"):
    st.write(usr_num)


txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )