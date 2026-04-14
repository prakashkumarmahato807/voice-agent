# stt.py
# Yeh file audio ko text mein convert karti hai

import os
from groq import Groq
from dotenv import load_dotenv

# .env file se API key lo
load_dotenv()

# Groq client banao
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(file_path):
    """
    Audio file lo aur text return karo
    file_path = audio file ka path
    """
    
    # Check karo file exist karti hai ya nahi
    if not os.path.exists(file_path):
        return "Error: Audio file nahi mili!"
    
    try:
        # Audio file kholo
        with open(file_path, "rb") as audio_file:
            
            # Groq Whisper model ko audio do
            result = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                language="en"  # English ke liye
            )
        
        # Text return karo
        return result.text
    
    except Exception as e:
        return f"Error aaya: {str(e)}"


# Test karne ke liye
if __name__ == "__main__":
    print("STT module ready hai!")
    print("API Key loaded:", os.getenv("GROQ_API_KEY") is not None)