# House Price Prediction Using Machine Learning

A Streamlit-based web application that predicts house prices based on user-input property details using a trained Machine Learning model built with Linear Regression.

Project Overview

This project uses housing data to estimate house prices based on various important features such as:

Bedrooms
Bathrooms
Square Foot Living Area
Lot Size
Floors
Waterfront Availability
View Rating
Condition
Grade
Basement Area
Built Year
Renovation Year
Zipcode
Latitude
Longitude

The model is trained using the King County House Sales Dataset and deployed through an interactive Streamlit application.

# Features
Interactive web interface using Streamlit
Real-time house price prediction
User-friendly input fields
Trained Linear Regression model
Pickle model integration (Model.pkl)
Accurate feature-based predictions
Deployable on Streamlit Cloud

# Technologies Used
Python
Streamlit
NumPy
Pandas
Scikit-learn
Pickle

# Machine Learning Model
Algorithm:

Linear Regression

Model Performance:
Training Accuracy (R² Score): ~70%
Testing Accuracy (R² Score): ~70%
Cross Validation Score: ~69–70%

Error Metrics:
Mean Absolute Error (MAE): ~127K
Mean Squared Error (MSE): Moderate predictive variance
Mean Absolute Percentage Error (MAPE): ~25%

Dataset Information
Dataset: King County House Data
Records: 21,613
Features Used: 16
Target Variable: Price

Selected Features:
bedrooms
bathrooms
sqft_living
sqft_lot
floors
waterfront
view
condition
grade
sqft_above
sqft_basement
yr_built
yr_renovated
zipcode
lat
long


# Project Structure

House-Price-Prediction-Using-Machine-Learning/
│
├── Project1/
│   ├── streamlit_app.py
│   ├── Model.pkl
│
├── README.md
└── requirements.txt
Installation & Setup

Clone Repository:
git clone https://github.com/M-Sudheer18/House-Price-Prediction-Using-Machine-Learning.git

Navigate:
cd House-Price-Prediction-Using-Machine-Learning/Project1

Install Dependencies:
pip install -r requirements.txt

Run Streamlit App:
streamlit run streamlit_app.py

Streamlit Deployment
Main File:
Project1/streamlit_app.py

Sample Inputs
Bedrooms: 3
Bathrooms: 2
Sqft Living: 2000
Sqft Lot: 5000
Floors: 2
Waterfront: No
View: 2
Condition: 3
Grade: 7


Output:
Estimated Price: $XXX,XXX
Future Improvements
Add Random Forest / XGBoost for better accuracy
Improve UI design
Add data visualizations
Feature importance graphs
Model comparison dashboard
Better handling of outliers
Currency formatting for output
Author

Sudheer Muthyala

Full Stack Developer Aspirant
Machine Learning Enthusiast
GitHub: M-Sudheer18
License

This project is open-source and available for educational and portfolio purposes.

Conclusion

This project demonstrates the practical implementation of:

Data Cleaning
Feature Selection
Regression Modeling
Model Serialization
Web Deployment

It serves as an excellent beginner-to-intermediate Machine Learning deployment project showcasing real-world house price prediction.
