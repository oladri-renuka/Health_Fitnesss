import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import re
import string

# Load Models & Datasets
pcos_model = joblib.load("xgboost_model.joblib")
diet = pd.read_csv("recipes.csv")
gym = pd.read_csv("gym recommendation.csv")

st.set_page_config(
    page_title="🏥 Health & Fitness App",  # Added hospital emoji
    layout="centered"
)

# Home Page
def home():
    st.title("👩‍⚕️ PCOS & Fitness Assistant")
    st.write("### Your AI-Based Health Companion")

    # Large Buttons for Navigation
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button("🔬 PCOS Prediction", use_container_width=True):
            st.session_state.page = "PCOS"

    with col2:
        if st.button("🥗 Diet Recommendation", use_container_width=True):
            st.session_state.page = "Diet"

    with col3:
        if st.button("🏋️ Exercise Plan", use_container_width=True):
            st.session_state.page = "Exercise"

    st.markdown("---")

# PCOS Prediction Page
def pcos_prediction():
    st.title("🔬 PCOS Prediction")
    st.sidebar.header("🩺 User Input Features")

    # Feature Descriptions
    st.sidebar.subheader("ℹ️ Feature Descriptions:")
    st.sidebar.markdown("""
    - **Cycle (R/I)**:  
      - 2: Regular  
      - 4: Irregular  
      - 5: Other (very rare cases)  
    - **Weight Gain (0/1)**:  
      - 0: No  
      - 1: Yes  
    - **Hair Growth (0/1)**:  
      - 0: No  
      - 1: Yes  
    - **Skin Darkening (0/1)**:  
      - 0: No  
      - 1: Yes  
    - **Fast Food (0/1)**:  
      - 0: No  
      - 1: Yes  
    - **Follicle No. (L)**: No. of follicles in the left ovary.  
    - **Follicle No. (R)**: No. of follicles in the right ovary.  
    """)

    # Collect User Input
    Cycle = st.sidebar.selectbox("Cycle (R/I)", (2, 4, 5))
    Weight_gain = st.sidebar.selectbox("Weight gain (Y/N)", (0, 1))
    Hair_growth = st.sidebar.selectbox("Hair growth (Y/N)", (0, 1))
    Skin_darkening = st.sidebar.selectbox("Skin darkening (Y/N)", (0, 1))
    Fast_food = st.sidebar.selectbox("Fast food (Y/N)", (0, 1))
    Follicle_No_L = st.sidebar.selectbox("Follicle No. (L)", list(range(0, 23)))
    Follicle_No_R = st.sidebar.selectbox("Follicle No. (R)", list(range(0, 21)))

    # Create DataFrame for Prediction
    df = pd.DataFrame({
        "Cycle(R/I)": [Cycle],
        "Weight gain(Y/N)": [Weight_gain],
        "hair growth(Y/N)": [Hair_growth],
        "Skin darkening (Y/N)": [Skin_darkening],
        "Fast food (Y/N)": [Fast_food],
        "Follicle No. (L)": [Follicle_No_L],
        "Follicle No. (R)": [Follicle_No_R],
    })

    # Display User Input
    st.subheader("📌 Your Input Data")
    st.write(df)

    # Make Prediction
    if st.button("📊 Predict PCOS"):
        prediction = pcos_model.predict(df)
        st.subheader("🔍 Prediction Result")
        st.success("✅ **PCOS Detected**" if prediction[0] == 1 else "❌ **No PCOS**")

    # Navigation Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"

# Diet Recommendation Page
def diet_recommendation():
    st.title("🥗 Personalized Meal Recommendation")

    # Collect User Input
    age = st.number_input("🎂 Enter your age:", min_value=1, step=1)
    sex = st.selectbox("⚥ Enter your sex:", ["Male", "Female"])
    weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, step=0.1)
    height = st.number_input("📏 Enter your height (cm):", min_value=50.0, step=0.1)
    activity_level = st.selectbox("🏃‍♂️ Activity Level:", ["Sedentary", "Lightly Active", "Moderate", "Very Active", "Extra Active"])
    goal = st.selectbox("🎯 Goal:", ["Weight Loss", "Weight Gain", "Maintenance"])
    diet_preference = st.text_input("🍛 Diet Preference (e.g., vegetarian, vegan):")
    allergies = st.text_area("🚫 Allergies (comma-separated):").split(",")

    # Recommendation Button
    if st.button("🔎 Get Meal Recommendations"):
        st.success("✅ Recommended meals will be displayed here!")  # Replace with actual recommendation logic

    # Navigation Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"

# Exercise Recommendation Page
def exercise_recommendation():
    st.title("🏋️ Exercise Plan Recommendation")

    # Collect User Input
    sex = st.selectbox("⚥ Select Gender", options=["Male", "Female"])
    age = st.slider("🎂 Select Age", min_value=10, max_value=80, value=25)
    height = st.number_input("📏 Enter Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
    weight = st.number_input("⚖️ Enter Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
    level = st.selectbox("🔥 Fitness Level", options=["Overweight", "Normal", "Obese", "Underweight"])
    fitness_goal = st.selectbox("🎯 Fitness Goal", options=["Weight Loss", "Weight Gain"])
    fitness_type = st.selectbox("🏋️ Fitness Type", options=["Cardio Fitness", "Muscular Fitness"])

    # Recommendation Button
    if st.button("💪 Get Exercise Plan"):
        st.success("✅ Recommended exercises will be displayed here!")  # Replace with actual recommendation logic

    # Navigation Button
    if st.button("🏠 Back to Home"):
        st.session_state.page = "Home"

# Initialize Session State
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Page Navigation
if st.session_state.page == "Home":
    home()
elif st.session_state.page == "PCOS":
    pcos_prediction()
elif st.session_state.page == "Diet":
    diet_recommendation()
elif st.session_state.page == "Exercise":
    exercise_recommendation()
