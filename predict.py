import pickle
import streamlit as st
from streamlit_option_menu import option_menu


with open('dd.pkl','rb') as file:
  clf1=pickle.load(file)  
 
with st.sidebar:
    selected = option_menu('Proactive Health Gaurd',

                           ['Welcome','Diabetes Prediction'],
                        
                           default_index=0)


if selected=='Welcome':
    st.image("logo1.png")
    st.title(":red[Diabetes Predictor]")
    st.title('Diabetes Prediction using ML')
    st.write(":blue[Diabetes mellitus refers to a group of diseases that affect how the body uses blood sugar (glucose). Glucose is an important source of energy for the cells that make up the muscles and tissues. It's also the brain's main source of fuel.]")



    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')



    diab_diagnosis = ''

    

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        prediction = clf1.predict([user_input])

        if prediction == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)    
    


if selected == 'Review':    
    st.title(":red[Review section]")
    st.write(":blue[Thank you for trying our app ,your every feedback matters]")
    st.text_area("Write your suggestions")
    st.write(":blue[how was your experience on a scale of 1 to 10.]")
    st.slider("",0,10)
