# Importing essential libraries and modules
from flask import Flask, render_template, request
import numpy as np
import pickle

# ==============================================================================================

# -------------------------LOADING THE TRAINED MODEL -----------------------------------------------

# Loading crop period prediction model
crop_period_model_path = 'models/RandomForest.pkl'
crop_period_model = pickle.load(open(crop_period_model_path, 'rb'))

# ===============================================================================================

# Custom function for crop period prediction
def predict_crop_period(features):
    """
    Predicts the period for planting and harvesting crops
    :params: features (list or array-like)
    :return: prediction (string)
    """
    # Your logic for predicting the crop period based on the input features
    # ...

# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------

app = Flask(__name__)

# render home page
@app.route('/')
def home():
    title = 'Crop Period Prediction App'
    return render_template('index.html', title=title)

# render crop period prediction form page
@app.route('/crop-period-predict')
def crop_period_predict():
    title = 'Crop Period Prediction'
    return render_template('crop_period_predict.html', title=title)

# render crop period prediction result page
@app.route('/crop-period-result', methods=['POST'])
def crop_period_result():
    title = 'Crop Period Prediction Result'

    if request.method == 'POST':
        # Assuming you have form fields like temperature, humidity, pH, etc.
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        water_availability = float(request.form['water_availability'])
        season = request.form['season']
        label = request.form['label']
        country = request.form['country']

        # Create a feature vector for prediction
        features = [temperature, humidity, ph, water_availability, season, label, country]

        # Use the crop period prediction model
        prediction = predict_crop_period(features)

        return render_template('crop_period_result.html', prediction=prediction, title=title)
        
    else:
        return render_template('try_again.html', title=title)

# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
