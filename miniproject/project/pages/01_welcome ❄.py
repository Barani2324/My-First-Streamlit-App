import streamlit as st

name = st.text_input("Please enter your name :smile: : ")
if name:
    st.write("Welcome to diet Assitance ", name ,":heart_eyes:")
    st.snow()

#BMI

def calculate_bmi(weight, height):
    bmi = weight / (height/100)**2
    return bmi

st.markdown("BMI Calculator")

weight = st.number_input('Enter your weight (kg):', min_value=30.0, max_value=300.0, step=0.1)
height = st.number_input('Enter your height (cm):', min_value=100.0, max_value=300.0, step=0.1)
age = st.number_input('Enter your age (years):', min_value=1, max_value=150, step=1)
gender = st.selectbox('Select your gender:', ['male', 'female'])

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        st.write(name ,"You are underweight")
    elif 18.5 <= bmi < 25:
        st.write(name , "You have a normal weight:sunglasses:")
    elif 25 <= bmi < 30:
        st.write(name , "You are overweight")
    else:
        st.write(name, "You are obese")

import streamlit as st


st.markdown("BMR Calculator")

def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        return None
    return bmr



if st.button('Calculate BMR'):
    bmr = calculate_bmr(weight, height, age, gender)
    if bmr:
        st.success(f'Your Basal Metabolic Rate (BMR) is {round(bmr, 2)} kcal/day.')
    else:
        st.warning('Please select your gender.')



import streamlit as st
from gtts import gTTS
from io import BytesIO
from pygame import mixer

# Define the Streamlit app
def app():
    
    # Create the welcome message
    message = "Please enter your Details to Know Your BODY MASS INDEX and BASAL METABOLIC RATE !"
    
    # Generate the audio file using Google Text-to-Speech (gTTS)
    audio_file = BytesIO()
    tts = gTTS(text=message, lang='en')
    tts.write_to_fp(audio_file)
    
    # Play the audio file using Pygame mixer
    audio_file.seek(0)
    mixer.init()
    mixer.music.load(audio_file)
    
    # Check if the welcome message has been played before
    if st.session_state.get('played_BMI', False) == False:
        mixer.music.play()
        st.session_state['played_BMI'] = True
    
if __name__ == "__main__":
    app()
