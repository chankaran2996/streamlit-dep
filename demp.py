import streamlit as st

# Title of the app
st.title("My First Streamlit App")

# Add a header
st.header("Welcome to my app!")

# Add some text
st.write("This is a basic Streamlit app.")

# Add an input box
user_input = st.text_input("Enter some text:")

# Display the user input
if user_input:
    st.write(f"You entered: {user_input}")

# Add a slider
number = st.slider("Pick a number", 0, 100, 50)

# Display the slider value
st.write(f"You picked: {number}")