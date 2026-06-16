import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
model = joblib.load("emotion_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(
    page_title="Social Media Insights",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Social Media Insights Through Big Data Analytics")

st.write(
    "Predict user emotions using Machine Learning and Social Media Analytics."
)

# User Inputs

age = st.number_input(
    "Age",
    min_value=10,
    max_value=100,
    value=22
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

platform = st.selectbox(
    "Platform",
    ["Instagram", "Twitter", "WhatsApp"]
)

daily_usage = st.number_input(
    "Daily Usage Time (minutes)",
    value=120
)

posts = st.number_input(
    "Posts Per Day",
    value=4
)

likes = st.number_input(
    "Likes Received Per Day",
    value=100
)

comments = st.number_input(
    "Comments Received Per Day",
    value=20
)

messages = st.number_input(
    "Messages Sent Per Day",
    value=30
)

if st.button("Predict Emotion"):

    sample = pd.DataFrame({
        'Age':[age],
        'Gender':[gender],
        'Platform':[platform],
        'Daily_Usage_Time (minutes)':[daily_usage],
        'Posts_Per_Day':[posts],
        'Likes_Received_Per_Day':[likes],
        'Comments_Received_Per_Day':[comments],
        'Messages_Sent_Per_Day':[messages]
    })

    prediction = model.predict(sample)

    emotion = label_encoder.inverse_transform(prediction)

    st.success(
        f"Predicted Emotion: {emotion[0]}"
    )

st.markdown("---")

st.subheader("Research Findings")

st.write("""
✅ Instagram interactions are predominantly linked to happiness.

✅ Twitter and WhatsApp show higher levels of anger and sadness.

✅ Moderate engagement correlates with positive emotional states.

✅ Excessive engagement may contribute to anxiety.

✅ XGBoost achieved approximately 98% classification accuracy.
""")

st.markdown("---")

st.subheader("Technologies Used")

st.write("""
Python • XGBoost • Scikit-Learn • Pandas • NumPy • Streamlit • Machine Learning
""")
st.subheader("MADE BY AYUSH SANKHYAN")
