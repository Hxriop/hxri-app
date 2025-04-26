# Install required packages (if not already installed)
# pip install TTS streamlit
pip install TTS

import streamlit as st
from TTS.api import TTS
import tempfile
import os

# Initialize TTS model (fast model)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

# Streamlit App
st.title("Hxri AI - Text to Voice 🎤")
st.write("Enter your text below, and listen to it!")

# Text input
text = st.text_area("Type something...", placeholder="Hello, welcome to Hxri AI!")

# Button to generate audio
if st.button("Convert to Voice"):
    if text.strip() == "":
        st.error("Please enter some text!")
    else:
        with st.spinner('Generating Audio...'):
            # Save audio to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
                tts.tts_to_file(text=text, file_path=fp.name)
                st.audio(fp.name)

        st.success("Here is your voice output!")

# Footer
st.caption("Made with ❤️ by Hxri AI")
