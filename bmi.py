import streamlit as st
st.title("Simple BMI Calculator using Streamlit")

weight = st.number_input("Enter your weight in kgs")

# take height input in meters
height = st.number_input('Meters')
 
try:
    bmi = weight / (height ** 2)
except:
    st.text("Enter some value of height")

if( st.button("Calculate BMI")):
    st.text("Your BMI Index is {}. ".format(bmi))

    if(bmi < 16):
        st.error("Ypu are extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Congratulations, You are Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.error("You are Overweight")
    else:
        st.error("You are Obese/ Extremely Overweight")