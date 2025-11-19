import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("xg_model.pkl")

st.title("⚽ Expected Goals (xG) Predictor")

st.markdown("Enter shot features below to estimate the xG value:")

# Numeric inputs
distance = st.number_input("Shot Distance (meters)", min_value=0.0, max_value=100.0, value=10.0)
angle = st.number_input("Shot Angle (degrees)", min_value=0.0, max_value=180.0, value=45.0)

# Binary inputs (checkboxes)
under_pressure = st.checkbox("Under Pressure?", value=False)
shot_first_time = st.checkbox("First Time Shot?", value=False)
shot_one_on_one = st.checkbox("One-on-One with GK?", value=False)

# Body part (one-hot encoded)
body_part = st.selectbox("Body Part", ["Head", "Left Foot", "Right Foot", "Other"])

# Technique (one-hot encoded)
technique = st.selectbox( "Shot Technique", 
                         ["Normal", "Backheel", "Diving Header", "Half Volley", "Lob","Overhead Kick", "Volley"])

# Position (one-hot encoded)
position = st.selectbox(
    "Player Position",
    [
        "Goalkeeper", "Center Back", "Left Back", "Right Back",
        "Left Wing Back", "Right Wing Back",
        "Left Defensive Midfield", "Right Defensive Midfield",
        "Center Defensive Midfield",
        "Left Midfield", "Center Midfield", "Right Midfield",
        "Left Attacking Midfield", "Center Attacking Midfield", "Right Attacking Midfield",
        "Left Center Forward", "Right Center Forward", "Secondary Striker"
    ]
)

# Period (first half, second half, etc.)
period = st.selectbox("Match Period", ["1", "2", "3", "4"])

# Initialize all features to 0
features = {
    'angle': angle,
    'distance': distance,
    'under_pressure': int(under_pressure),
    'shot_first_time': int(shot_first_time),
    'shot_one_on_one': int(shot_one_on_one)
}

# Add one-hot encoded features
# Body parts
for bp in ['Head', 'Left Foot', 'Right Foot', 'Other']:
    features[f'shot_body_part_{bp}'] = 1 if body_part == bp else 0

# Techniques
for t in ['Backheel', 'Diving Header', 'Half Volley', 'Lob', 'Normal', 'Overhead Kick', 'Volley']:
    features[f'shot_technique_{t}'] = 1 if technique == t else 0

# Positions
positions = [
    "Center Attacking Midfield", "Center Back", "Center Defensive Midfield", "Center Forward", "Center Midfield",
    "Goalkeeper", "Left Attacking Midfield", "Left Back", "Left Center Forward", "Left Center Midfield",
    "Left Defensive Midfield", "Left Midfield", "Left Wing", "Left Wing Back",
    "Right Attacking Midfield", "Right Back", "Right Center Back", "Right Center Forward", "Right Center Midfield",
    "Right Defensive Midfield", "Right Midfield", "Right Wing", "Right Wing Back",
    "Secondary Striker"
]
for pos in positions:
    features[f'position_{pos}'] = 1 if position == pos else 0

# Periods
for p in ['1', '2', '3', '4']:
    features[f'period_{p}'] = 1 if period == p else 0

# Make prediction
if st.button("Predict xG"):
    input_df = pd.DataFrame([features])
    # Ensure all expected columns exist (fill any missing with 0)
    expected_features = model.get_booster().feature_names
    for col in expected_features:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_features]

    # Predict
    xg_pred = model.predict_proba(input_df)[:, 1][0]
    st.success(f"Estimated xG: **{xg_pred:.3f}**")
