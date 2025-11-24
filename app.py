# -*- coding: utf-8 -*-
"""
Created on Tue Nov 25 03:48:46 2025

@author: Yousuf Traders
"""

import numpy as np
import pickle
import streamlit as st


loaded_model = pickle.load(open('logistic_model.pkl', 'rb'))
loaded_scaler = pickle.load(open('scaler.pkl','rb'))


# Creating a function for Prediciton

def cancer_prediction(input_data):
    
    # Changing The Data into Numpy Array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape The Array as we are Predicting
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Scale the input using loaded scaler
    scaled_input = loaded_scaler.transform(input_data_reshaped)

    prediction = loaded_model.predict(scaled_input)

    if (prediction[0] == 0):
      return("The Person has Benign Tumor Breast Cancer")
    else:
      return("The Person has Malignant Tumor Breast cancer")
  
    
def main():
    
    # radius_mean,"texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"
    
    # Giving a title
    st.title('Breast Cancer Prediction Web App')
    
    # Getting the Data as input from user
    radius_mean = st.text_input('Radius Mean')
    texture_mean = st.text_input('Texture Mean')
    perimeter_mean = st.text_input('Perimeter Mean')
    area_mean = st.text_input('Area Mean')
    smoothness_mean = st.text_input('Smoothness Mean')
    compactness_mean = st.text_input('Compactness Mean')
    concavity_mean = st.text_input('Concavity Mean')
    concave_points_mean = st.text_input('Concave Points Mean')
    symmetry_mean = st.text_input('Symmetry Mean')
    fractal_dimension_mean = st.text_input('Fractal Dimension Mean')
    radius_se = st.text_input('Radius SE')
    texture_se = st.text_input('Texture SE')
    perimeter_se = st.text_input('Perimeter SE')
    area_se = st.text_input('Area SE')
    smoothness_se = st.text_input('Smoothness SE')
    compactness_se = st.text_input('Compactness SE')
    concavity_se = st.text_input('Concavity SE')
    concave_points_se = st.text_input('Concave Points SE')
    symmetry_se = st.text_input('Symmetry SE')
    fractal_dimension_se = st.text_input('Fractal Dimension SE')
    radius_worst = st.text_input('Radius Worst')
    texture_worst = st.text_input('Texture Worst')
    perimeter_worst = st.text_input('Perimeter Worst')
    area_worst = st.text_input('Area Worst')
    smoothness_worst = st.text_input('Smoothness Worst')
    compactness_worst = st.text_input('Compactness Worst')
    concavity_worst = st.text_input('Concavity Worst')
    concave_points_worst = st.text_input('Concave Points Worst')
    symmetry_worst = st.text_input('Symmetry Worst')
    fractal_dimension_worst = st.text_input('Fractal Dimension Worst')
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a Button
    
        
    if st.button('Breast Cancer Test Result:'):
        # Convert all inputs to float
        try:
            input_data = [
                          float(radius_mean), float(texture_mean), float(perimeter_mean), float(area_mean),
                          float(smoothness_mean), float(compactness_mean), float(concavity_mean),
                          float(concave_points_mean), float(symmetry_mean), float(fractal_dimension_mean),
                          float(radius_se), float(texture_se), float(perimeter_se), float(area_se),
                          float(smoothness_se), float(compactness_se), float(concavity_se),
                          float(concave_points_se), float(symmetry_se), float(fractal_dimension_se),
                          float(radius_worst), float(texture_worst), float(perimeter_worst), float(area_worst),
                          float(smoothness_worst), float(compactness_worst), float(concavity_worst),
                          float(concave_points_worst), float(symmetry_worst), float(fractal_dimension_worst)]
            
            diagnosis = cancer_prediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid numeric values for all fields."
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()

