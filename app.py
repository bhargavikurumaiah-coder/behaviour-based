import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import predict_segment
from utils import preprocess_data

# -------------------------------
# TITLE
# -------------------------------
st.set_page_config(page_title="Behavior Segmentation App", layout="centered")
st.title("📊 Behavior-Based User Segmentation")

st.markdown("Analyze user activity signals and classify engagement level")

# -------------------------------
# USER INPUT
# -------------------------------
st.sidebar.header("User Input")

clicks = st.sidebar.slider("Number of Clicks", 0, 100, 10)
time_spent = st.sidebar.slider("Time Spent (minutes)", 0, 300, 30)
activity = st.sidebar.slider("Activity Frequency", 0, 50, 5)

input_data = pd.DataFrame({
    "clicks": [clicks],
    "time_spent": [time_spent],
    "activity": [activity]
})

st.subheader("📥 Input Data")
st.write(input_data)

# -------------------------------
# PROCESS DATA
# -------------------------------
processed_data = preprocess_data(input_data)

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("Predict Segment"):
    result = predict_segment(processed_data)

    st.subheader("🎯 Predicted Segment")
    st.success(result)

    # -------------------------------
    # VISUALIZATION
    # -------------------------------
    st.subheader("📈 Signal Visualization")

    fig, ax = plt.subplots()
    ax.bar(["Clicks", "Time", "Activity"], 
           [clicks, time_spent, activity])
    ax.set_title("User Behavior Signals")

    st.pyplot(fig)