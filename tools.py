# tools.py
# Yeh file actual kaam karegi intent ke hisaab se

import os
from groq import Groq
from dotenv import load_dotenv

# .env se API key lo
load_dotenv()

# Groq client banao
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Output folder — yahan sab files banegi
OUTPUT_DIR = "output/"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def create_file(text):
    """
    Nayi file banao
    """
    try:
        # AI se filename lo
        prompt = f"""
        Extract a simple filename from this text.
        Rules:
        - Only filename with extension
        - No spaces, use underscore
        - Example: my_file.txt or notes.py
        - Only return filename, nothing else
        
        Text: "{text}"
        Filename:
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        filename = response.choices[0].message.content.strip()
        filename = filename.replace("\n", "").strip()

        # Path banao
        filepath = os.path.join(OUTPUT_DIR, filename)

        # File banao
        with open(filepath, "w") as f:
            f.write(f"# File created by Voice Agent\n")
            f.write(f"# Command: {text}\n")

        return f"File bana di: {filepath}"

    except Exception as e:
        return f"Error: {str(e)}"


def write_code(text):
    """
    Code generate karo aur file mein save karo
    """
    try:
        # AI se code lo
        prompt = f"""
        Write Python code for this request.
        Rules:
        - Only write code
        - No explanation
        - Add comments in code
        
        Request: "{text}"
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        code = response.choices[0].message.content.strip()

        # Code backticks remove karo agar ho
        code = code.replace("```python", "").replace("```", "").strip()

        # File mein save karo
        filepath = os.path.join(OUTPUT_DIR, "generated_code.py")
        with open(filepath, "w") as f:
            f.write(code)

        return code, filepath

    except Exception as e:
        return f"Error: {str(e)}", None


def summarize(text):
    """
    Text ka summary do
    """
    try:
        prompt = f"""
        Summarize this text in 3-4 simple lines.
        Be clear and concise.
        
        Text: "{text}"
        
        Summary:
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:
        return f"Error: {str(e)}"


def general_chat(text):
    """
    Normal conversation
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()
        return reply

    except Exception as e:
        return f"Error: {str(e)}"


# Test karne ke liye
if __name__ == "__main__":

    print("Tools Test:")
    print("-" * 30)

    # Test 1 - File banao
    print("Test 1 - File Creation:")
    result = create_file("Create a file named my_notes")
    print(result)
    print("-" * 30)

    # Test 2 - Code likho
    print("Test 2 - Code Writing:")
    code, path = write_code("Write a function to add two numbers")
    print(f"Code saved at: {path}")
    print(f"Code preview:\n{code[:100]}...")
    print("-" * 30)

    # Test 3 - Summarize
    print("Test 3 - Summarize:")
    summary = summarize(
        "Artificial Intelligence is transforming the world. "
        "It is being used in healthcare, education, and business. "
        "AI can process large amounts of data quickly and accurately."
    )
    print(f"Summary: {summary}")
    print("-" * 30)

    # Test 4 - Chat
    print("Test 4 - General Chat:")
    reply = general_chat("What is Python programming?")
    print(f"Reply: {reply[:150]}...")
    print("-" * 30)