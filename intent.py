# intent.py
# Yeh file samjhegi ki user kya chahta hai

import os
from groq import Groq
from dotenv import load_dotenv

# .env se API key lo
load_dotenv()

# Groq client banao
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_intent(text):
    """
    Text lo aur intent return karo
    4 intents hain:
    - create_file
    - write_code
    - summarize
    - general_chat
    """

    prompt = f"""
    You are an intent classifier.
    Classify the following text into ONLY ONE of these intents:
    - create_file
    - write_code
    - summarize
    - general_chat

    Rules:
    - Reply with ONLY the intent label
    - No explanation needed
    - No extra text

    Text: "{text}"

    Intent:
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1
        )

        # Intent text lo
        intent = response.choices[0].message.content.strip().lower()

        # Clean karo extra spaces ya newlines
        intent = intent.replace("\n", "").strip()

        # Check karo valid intent hai ya nahi
        valid_intents = [
            "create_file",
            "write_code", 
            "summarize",
            "general_chat"
        ]

        if intent in valid_intents:
            return intent
        else:
            return "general_chat"

    except Exception as e:
        return f"Error: {str(e)}"


# Test karne ke liye
if __name__ == "__main__":
    
    # Test cases
    test_texts = [
        "Create a new python file",
        "Write code for a calculator",
        "Summarize this text about AI",
        "Hello how are you"
    ]

    print("Intent Detection Test:")
    print("-" * 30)

    for text in test_texts:
        intent = detect_intent(text)
        print(f"Text: {text}")
        print(f"Intent: {intent}")
        print("-" * 30)