import streamlit as st
import os
import tempfile
from stt import transcribe_audio
from intent import detect_intent
from tools import create_file, write_code, summarize, general_chat

# Page setup
st.set_page_config(
    page_title="Voice AI Agent",
    page_icon="🎙️",
    layout="centered"
)

# Title
st.title("🎙️ Voice Controlled AI Agent")
st.subheader("Mem0 Internship Assignment")
st.markdown("---")

# Instructions
st.info("""
**Kaise use karein:**
1. Audio file upload karo (.wav ya .mp3)
2. Agent automatically samjhega kya karna hai
3. Result neeche dikhega
""")

# Audio file upload
st.markdown("### 📁 Audio File Upload Karo")
audio_file = st.file_uploader(
    "Audio file choose karo",
    type=["wav", "mp3", "m4a"],
    help="Supported formats: WAV, MP3, M4A"
)

# Process karo jab file upload ho
if audio_file is not None:

    # Audio player dikhao
    st.audio(audio_file)

    # Process button
    if st.button("🚀 Process Karo", type="primary"):

        # Step 1 - Transcribe
        with st.spinner("🎧 Audio sun raha hun..."):

            # Temp file banao
            suffix = "." + audio_file.name.split(".")[-1]
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name

            # Transcribe karo
            transcribed_text = transcribe_audio(tmp_path)

            # Temp file delete karo
            os.unlink(tmp_path)

        # Transcription dikhao
        st.markdown("### 📝 Transcribed Text")
        st.success(transcribed_text)

        # Step 2 - Intent detect karo
        with st.spinner("🧠 Samajh raha hun..."):
            intent = detect_intent(transcribed_text)

        # Intent dikhao
        st.markdown("### 🎯 Detected Intent")

        # Intent ke hisaab se color
        if intent == "create_file":
            st.info(f"📄 Intent: **{intent}**")
        elif intent == "write_code":
            st.warning(f"💻 Intent: **{intent}**")
        elif intent == "summarize":
            st.success(f"📋 Intent: **{intent}**")
        else:
            st.info(f"💬 Intent: **{intent}**")

        # Step 3 - Execute karo
        st.markdown("### ⚡ Action aur Result")

        with st.spinner("🔧 Kaam kar raha hun..."):

            # Intent ke hisaab se tool call karo
            if intent == "create_file":
                result = create_file(transcribed_text)
                st.success(f"✅ {result}")

            elif intent == "write_code":
                code, filepath = write_code(transcribed_text)

                if filepath:
                    st.success(f"✅ Code file save ho gayi: {filepath}")
                    st.markdown("**Generated Code:**")
                    st.code(code, language="python")
                else:
                    st.error(code)

            elif intent == "summarize":
                summary = summarize(transcribed_text)
                st.success("✅ Summary ready hai!")
                st.markdown("**Summary:**")
                st.write(summary)

            elif intent == "general_chat":
                reply = general_chat(transcribed_text)
                st.success("✅ Response ready hai!")
                st.markdown("**Response:**")
                st.write(reply)

        st.markdown("---")
        st.balloons()
        st.success("🎉 Sab kaam ho gaya!")

# Sidebar mein info
with st.sidebar:
    st.markdown("### ℹ️ Project Info")
    st.markdown("""
    **Voice AI Agent**
    
    **Models Used:**
    - STT: Groq Whisper
    - LLM: LLaMA 3.3 70B
    
    **Supported Intents:**
    - 📄 Create File
    - 💻 Write Code
    - 📋 Summarize
    - 💬 General Chat
    
    **Output Folder:**
    - All files saved in `output/`
    """)

    st.markdown("---")
    st.markdown("**Output Files:**")

    # Output folder ki files dikhao
    output_files = os.listdir("output/") if os.path.exists("output/") else []
    if output_files:
        for f in output_files:
            st.text(f"📄 {f}")
    else:
        st.text("Abhi koi file nahi hai")