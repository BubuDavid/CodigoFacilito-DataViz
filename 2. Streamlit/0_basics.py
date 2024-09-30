import time

import numpy as np
import pandas as pd
import streamlit as st

# Title and Header
st.title("Streamlit Basics Demo")
st.header("Explore the basic functionalities of Streamlit")

# Text
st.subheader("Displaying Text")
st.text("This is simple text.")
st.markdown("This is **Markdown** text with _italics_ and **bold**.")
st.caption("This is a small caption.")
st.code("print('Hello, Streamlit!')", language="python")

# Interactive Widgets
st.subheader("Widgets for User Interaction")

# Button
if st.button("Click me!"):
    st.write("Button clicked!")

# Checkbox
agree = st.checkbox("I agree")
if agree:
    st.write("You agreed!")

# Radio buttons
genre = st.radio("Choose your favorite genre:", ("Adventure", "Sci-fi", "Fantasy"))
st.write(f"You selected {genre}")

# Selectbox
option = st.selectbox(
    "Which is your favorite programming language?", ["Python", "JavaScript", "C++", "Java", "Other"]
)
st.write(f"You selected {option}")

# Slider
value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {value}")

# Text input
name = st.text_input("What's your name?")
st.write(f"Hello, {name}!")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120)
st.write(f"Your age is: {age}")

# Date input
date = st.date_input("Select a date")
st.write(f"You selected: {date}")

# Time input
current_time = st.time_input("Select a time")
st.write(f"You selected: {current_time}")

# Charts and Plots
st.subheader("Charts and Visualizations")

# Line chart
data = np.random.randn(100, 3)
st.line_chart(data)

# Bar chart
st.bar_chart(data)

# Map (for geographical data)
columns = pd.Series(["lat", "lon"])
st.subheader("Map Example")
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=columns)
st.map(map_data)

# Dataframes and Tables
st.subheader("Displaying Data")

# DataFrame
df = pd.DataFrame(
    {"Column A": np.random.randn(5), "Column B": np.random.randn(5), "Column C": np.random.randn(5)}
)
st.write("DataFrame Example:")
st.dataframe(df)

# Table
st.write("Static Table Example:")
st.table(df)

# Progress Bar
st.subheader("Progress and Status")

# progress = st.progress(0)
# for i in range(100):
#     time.sleep(0.05)
#     progress.progress(i + 1)

# Success, Info, Warning, Error messages
st.success("Success message!")
st.info("This is an informational message.")
st.warning("This is a warning.")
st.error("This is an error.")

# Sidebar
st.sidebar.title("Sidebar Example")
st.sidebar.write("You can add widgets here as well!")

sidebar_option = st.sidebar.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.sidebar.write(f"Sidebar option selected: {sidebar_option}")

st.sidebar.slider("Select a range in sidebar", 0, 50, (10, 40))

# File Upload
st.subheader("File Upload Example")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Uploaded file contents:")
    st.dataframe(df_uploaded)

# End of the app
st.write("🎉 You have reached the end of the demo!")
