import streamlit as st
import pandas as pd
option = st.selectbox(
    'Please select a disease to Know your diet chart for keep your day Healthy :smile:',
    ('please select your option','Diabetic','type 1 diabetes', 'Blood Pressure', 
     'High Cholesterol','kidney failure','Kidney Stone','PCOD' , 'PCOS','Thyroid', 
     'Celiac Disease','Liver Cirrhosis','Asthma', 'Breast cancer' , 'Cardiac Patients',
     'chicken pox','copd', 'eczema', 'Measles', 'psoriasis', 'tinea versicolor' ))

disease = st.write('You selected a diet chart For:', option)


data = pd.read_excel("C:/Users/ADMIN/miniproject/project/Data.xlsx")
data['Days'] = [ "Day_1", "Day_2" , "Day_3" , "Day_4" , "Day_5" , "Day_6" , "Day_7"]
data.set_index("Days" , inplace=True)

if option == "Diabetic":
    st.write(data[[ "Diebetic"]])
if option == "Blood Pressure":
    st.write(data[[ "Blood Pressure"]])
if option == "High Cholesterol":
    st.write(data[[ "High Cholesterol"]])
if option == "kidney failure":
    st.write(data[[ "kidney failure"]])
if option == "Kidney Stone":
    st.write(data[[ "Kidney Stone"]])
if option == "PCOD":
    st.write(data[[ "PCOD"]])
if option == "PCOS":
    st.write(data[[ "PCOS"]])
if option == "Thyroid":
    st.write(data[[ "Thyroid"]])
if option == "Celiac Disease":
    st.write(data[[ "Celiac Disease"]])
if option == "Liver Cirrhosis":
    st.write(data[[ "Liver Cirrhosis"]])
if option == "Asthma":
    st.write(data[["Asthma"]])
if option == "Breast cancer":
    st.write(data[[ "Breast cancer"]])
if option == "Cardiac Patients":
    st.write(data[[ "Cardiac Patients"]])
if option == "chicken pox":
    st.write(data[["chicken pox"]])
if option == "copd":
    st.write(data[["copd"]])
if option == "eczema":
    st.write(data[[ "eczema"]])
if option == "Measles":
    st.write(data[["Measles"]])
if option == "psoriasis":
    st.write(data[[ "psoriasis"]])
if option == "tinea versicolor":
    st.write(data[[ "tinea versicolor"]])
if option == "type 1 diabetes":
    st.write(data[["type 1 diabetes"]])




import streamlit as st
from gtts import gTTS
from io import BytesIO
from pygame import mixer

# Define the Streamlit app
def app():

    
    # Create the welcome message

    message_1 = "Here is the Diet chart for !"
    message = option
    
    # Generate the audio file using Google Text-to-Speech (gTTS)
    audio_file = BytesIO()
    tts = gTTS(text = message_1 + message, lang='en')
    tts.write_to_fp(audio_file)
    
    # Play the audio file using Pygame mixer
    audio_file.seek(0)
    mixer.init()
    mixer.music.load(audio_file)
    mixer.music.play()
    
if __name__ == "__main__":
    app()
