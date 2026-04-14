# stt.py


import os
from groq import Groq
from dotenv import load_dotenv

# Take API from .env
load_dotenv()

# Make Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(file_path):
    """
    Audio file lo aur text return karo
    file_path = path of audio file 
    """
    
    # Check Whether the file exit or not
    if not os.path.exists(file_path):
        return "Error: Audio file not found!"
    
    try:
        # Open Audio file 
        with open(file_path, "rb") as audio_file:
            
            # Give audio to Groq Whisper model 
            result = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                language="en"  # For English 
            )
        
        # Return text
        return result.text
    
    except Exception as e:
        return f"Error : {str(e)}"


# For Test 
if __name__ == "__main__":
    print("STT module ready hai!")
    print("API Key loaded:", os.getenv("GROQ_API_KEY") is not None)