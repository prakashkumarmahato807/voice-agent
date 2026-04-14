# intent.py


import os
from groq import Groq
from dotenv import load_dotenv

# Take API from .env
load_dotenv()

# Make Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_intent(text):
    """
    Take Text and return intent 
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

        # Take Intent text 
        intent = response.choices[0].message.content.strip().lower()

        # Clean extra spaces or newlines
        intent = intent.replace("\n", "").strip()

        # Check whether valid intent or not
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


# For Test
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