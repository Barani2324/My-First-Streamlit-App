import streamlit as st
st.balloons()



st.title("Welcome to Nutritious Diet Assistance")

from PIL import Image

image = Image.open('C:/Users/ADMIN/miniproject/project/image.png')

st.image(image)


import streamlit as st
from gtts import gTTS
from io import BytesIO
from pygame import mixer

# Define the Streamlit app
def app():
    
    # Create the welcome message
    message = "Welcome to Nutritious Diet Assistance!"

    # Generate the audio file using Google Text-to-Speech (gTTS)
    audio_file = BytesIO()
    tts = gTTS(text=message, lang='en')
    tts.write_to_fp(audio_file)
    
    # Play the audio file using Pygame mixer
    audio_file.seek(0)
    mixer.init()
    mixer.music.load(audio_file)
    
    # Check if the welcome message has been played before
    if st.session_state.get('played_welcome', False) == False:
        mixer.music.play()
        st.session_state['played_welcome'] = True
    
if __name__ == "__main__":
    app()
