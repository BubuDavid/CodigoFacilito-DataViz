import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pydeck as pdk

# Title
st.title("System Failure Reports Dashboard")
st.write("This app simulates system failures across the globe and visualizes the data.")

# Generate Fake Data for System Failures
def generate_fake_data(n_reports):
    np.random.seed(42)
    
    # Generate fake locations (latitude, longitude)
    latitudes = np.random.uniform(-90, 90, n_reports)
    longitudes = np.random.uniform(-180, 180, n_reports)
    
    # Generate random report texts
    reasons = [
        "Server down", "High CPU usage", "Network latency", "Memory leak detected",
        "Database connection failure", "API timeout", "Disk I/O bottleneck",
        "Authentication failure", "Unexpected restart", "Service overload"
    ]
    descriptions = np.random.choice(reasons, n_reports, replace=True)
    
    # Generate fake timestamps
    timestamps = pd.date_range("2023-09-01", periods=n_reports, freq="S")
    
    # Create DataFrame
    data = pd.DataFrame({
        "LAT": latitudes,
        "LON": longitudes,
        "Description": descriptions,
        "Timestamp": timestamps
    })
    
    return data

# Generate a random number of reports
n_reports = st.slider("Number of Reports to Simulate", 100, 1000, 500)
data = generate_fake_data(n_reports)

# Map Visualization
st.subheader("🗺️ Map of System Failures")
st.write("This map shows the locations of the reported system failures across the globe.")
st.map(data[['LAT', 'LON']])

# PyDeck Map (more detailed)
st.subheader("🌍 PyDeck Map View of Failures")
view_state = pdk.ViewState(latitude=0, longitude=0, zoom=1.5)
layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position=["LON", "LAT"],
    get_radius=50000,
    get_color=[200, 30, 0, 160],
    pickable=True
)
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

# Reports per Second Visualization
st.subheader("📈 Reports Per Second")
st.write("This line chart shows the number of system failures over time.")

# Aggregate the data per second
reports_per_second = data.groupby(pd.Grouper(key="Timestamp", freq="S")).size()
st.line_chart(reports_per_second)

# Word Cloud for Failure Descriptions
st.subheader("🌩️ Word Cloud of Failure Descriptions")
st.write("This word cloud shows the most common reasons for system failures.")

# Generate word cloud
wordcloud = WordCloud(background_color="white", width=800, height=400).generate(" ".join(data["Description"]))

# Display word cloud using Matplotlib
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# Progress Bar (for fun)
st.subheader("Simulating real-time system reports")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)

st.success("Simulation Complete!")

