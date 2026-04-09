import streamlit as st
import pickle as pic
import numpy as np

st.title("House Price Prediction")
st.write("House Price Prediction Machine Learning Model")
st.subheader("Enter House Details")
model = pic.load(open("Model.pkl", "rb"))

# User Inputs
# ['bedrooms',
#  'bathrooms',
#  'sqft_living',
#  'sqft_lot',
#  'floors',
#  'waterfront',
#  'view',
#  'condition',
#  'grade',
#  'sqft_above',
#  'sqft_basement',
#  'yr_built',
#  'yr_renovated',
#  'zipcode',
#  'lat',
#  'long']

# Bedrooms
bedrooms = st.number_input(
    "Enter No.of Bedrooms",
    min_value=0,
    max_value=None,
    value=0,
    step=1
)

# bathrooms
bathrooms = st.number_input(
    "Enter No.of Bathrooms",
    min_value=0,
    max_value=None,
    value=0,   # Value used for int, float --> int value = int(1), float value = float(1.0)
    step=1
)

#  sqft_living
sqft_living = st.number_input(
    "Enter Sqft Living Area",
    min_value=0,
    max_value=None,
    value=0,
    step=50
)


#  sqft_lot
sqft_lot = st.number_input(
    "Enter Sqft Lot",
    min_value=0,
    max_value=None,
    value=0,
    step=100
)

#  floors
floors = st.number_input(
    "Enter No.of Floors",
    min_value=1,
    max_value=None,
    value=1,
    step=1
)

#  waterfront
waterfront = 1 if st.checkbox('Is Waterfront Available!') else 0


#  view
view = st.number_input(
    "Enter Views",
    min_value=0,
    max_value=None,
    value=0,
    step=1
)

#  condition
condition = st.number_input(
    "Enter Condition",
    min_value=1,
    max_value=None,
    value=1,
    step=1
)

#  grade
grade = st.number_input(
    "Enter Grade",
    min_value=1,
    max_value=None,
    value=1,
    step=1
)

#  sqft_above
sqft_above = st.number_input(
    "Enter Sqft Above",
    min_value=0,
    max_value=None,
    value=0,
    step=200
)

#  sqft_basement
sqft_basement = st.number_input(
    "Enter Sqft Basement",
    min_value=0,
    max_value=None,
    value=0,
    step=200
)

#  yr_built
yr_built = st.number_input(
    "Enter House Built Year",
    min_value=1900,
    max_value=2025,
    value=2000,
    step=1
)

#  yr_renovated
yr_renovated = st.number_input(
    "Enter the House Renovated Year",
    min_value=0,
    max_value=2025,
    value=0,
    step=1
)

#  zipcode
zipcode = st.number_input(
    "Enter Zipcode",
    min_value=10000,
    max_value=99999,
    value=67895,
    step=1
)

#  latitude
latitude = st.number_input(
    "Enter House Latitude",
    min_value=-90.0,
    max_value=90.0,
    value=47.159300,
    step=0.000001,
    format="%.6f"
)

#  Longitude
longitude = st.number_input(
    "Enter House Longitude",
    min_value=-180.0,
    max_value=180.0,
    value=-122.519000,
    step=0.000001,
    format="%.6f"
)



features = np.array([[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        grade,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated,
        zipcode,
        latitude,
        longitude
]])


if st.button("Predict Price"):
    price_prediction = model.predict(features)[0]
    st.success(f"Estimated Price : {price_prediction}")