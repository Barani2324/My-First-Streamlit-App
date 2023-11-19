import streamlit as st

from PIL import Image

option = option = st.selectbox(
    'Please select a disease to Know your diet chart with calories :smile:',
    ('please select your option','Diabetic','type 1 diabetes', 'Blood Pressure', 
     'High Cholesterol','kidney failure','Kidney Stone','PCOD' , 'PCOS','Thyroid', 
     'Celiac Disease','Liver Cirrhosis','Asthma', 'Breast cancer' , 'Cardiac Patients',
     'chicken pox','copd', 'eczema', 'Measles', 'psoriasis', 'tinea versicolor' ))

if option == "Diabetic":
    image = Image.open('C:/Users/ADMIN/miniproject/project/diabetic.png')
    st.image(image)
if option == "type 1 diabetes":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Dia_Type1.png')
    st.image(image)
if option == "Blood Pressure":
    image = Image.open('C:/Users\ADMIN/miniproject/project/High_blood_pressure.png')
    st.image(image)
if option == "High Cholesterol":
    image = Image.open('C:/Users/ADMIN/miniproject/project/high_chelostrol.png')
    st.image(image)
if option == "kidney failure":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Kindney_failure.png')
    st.image(image)
if option == "Kidney Stone":
    image = Image.open('C:/Users/ADMIN/miniproject/project/kidney_stone.png')
    st.image(image)
if option == "PCOD":
    image = Image.open('C:/Users/ADMIN/miniproject/project/PCOD.png')
    st.image(image)
if option == "PCOS":
    image = Image.open('C:/Users/ADMIN/miniproject/project/pcos.png')
    st.image(image)
if option == "Thyroid":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Tyroid.png')
    st.image(image)
if option == "Celiac Disease":
    image = Image.open('C:/Users/ADMIN/miniproject/project/celiac.png')
    st.image(image)
if option == "Liver Cirrhosis":
    image = Image.open('C:/Users/ADMIN/miniproject/project/cirrhosis.png')
    st.image(image)
if option == "Asthma":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Asthma.png')
    st.image(image)
if option == "Breast cancer":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Breast_cancer.png')
    st.image(image)
if option == "Cardiac Patients":
    image = Image.open('C:/Users/ADMIN/miniproject/project/cardiac_dis.png')
    st.image(image)
if option == "chicken pox":
    image = Image.open('C:/Users/ADMIN/miniproject/project/chickenpox.png')
    st.image(image)
if option == "copd":
    image = Image.open('C:/Users/ADMIN/miniproject/project/copd.png')
    st.image(image)
if option == "eczema":
    image = Image.open('C:/Users/ADMIN/miniproject/project/eczema.png')
    st.image(image)
if option == "Measles":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Measles.png')
    st.image(image)
if option == "psoriasis":
    image = Image.open('C:/Users/ADMIN/miniproject/project/psoriasis.png')
    st.image(image)
if option == "tinea versicolor":
    image = Image.open('C:/Users/ADMIN/miniproject/project/Tina_vascular.png')
    st.image(image)

import streamlit as st
from gtts import gTTS
from io import BytesIO
from pygame import mixer

# Define the Streamlit app
def app():
    
    # Create the welcome message
    message = "Please select option to know the calories which is corresponding to your Diet chart!"
    
    # Generate the audio file using Google Text-to-Speech (gTTS)
    audio_file = BytesIO()
    tts = gTTS(text=message, lang='en')
    tts.write_to_fp(audio_file)
    
    # Play the audio file using Pygame mixer
    audio_file.seek(0)
    mixer.init()
    mixer.music.load(audio_file)
    
    # Check if the welcome message has been played before
    if st.session_state.get('played', False) == False:
        mixer.music.play()
        st.session_state['played'] = True
    
if __name__ == "__main__":
    app()




   
