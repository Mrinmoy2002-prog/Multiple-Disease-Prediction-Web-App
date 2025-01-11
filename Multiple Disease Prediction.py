# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 11:45:28 2025

@author: mrinm
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading all the models

diabetes_model = pickle.load(open('C:/Users/mrinm/OneDrive/Desktop/Me/ML Project/Multiple Disease Prediction System/Saved Models/trained_model.sav','rb'))
Perkisons_model = pickle.load(open('C:/Users/mrinm/OneDrive/Desktop/Me/ML Project/Multiple Disease Prediction System/Saved Models/trained_model_perkinson.sav','rb'))



# Creating Sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           
                           #Sub Pages
                           ['Diabetes Prediction','Perkisons Prediction'],
                           
                           #Icons Before the sub-pages name
                           icons = ['activity', 'person'],
                           
                           #Default idex means where from it starts when we open the page : 0->diabetes prediction, 1->perkisons prediction
                           default_index = 0) 
    
# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):  #If user selects the diabetes prediction then generate a page with title
    
    #page title
    st.title('Diabetes Prediction Using ML')
    
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col1:
        SkinThickness = st.text_input('Skin Thickness level')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col2:
        Age = st.text_input('What is your Age')
    
    with col3:
        BloodPressure = st.text_input('BloodPressure level')
    with col3:
        BMI = st.text_input('BMI value')
    
 
    #code for prediction 
    diagnosis = ''    #This will store the output text
    
    # creating a button for prediction
    if st.button('Diabetes test results'):
        diagnosis = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
    st.success(diagnosis) #This is used to display the result
    
    
    
if (selected == 'Perkisons Prediction'):
    
    #page title
    st.title('Perkisons Prediction Using ML')