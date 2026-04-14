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
st.subheader("Mem0 Internship Assignment - Voice AI Agent")
st.markdown("---")

# Instructions
st.info("""
**How to use:**
1. Upload an audio file (.wav or .mp3)
2. The agent will automatically detect your intent
3. Results will be displayed below
""")

# Audio file upload
st.markdown("### 📁 Upload Audio File")
audio_file = st.file_uploader(
    "Choose an audio file",
    type=["wav", "mp3", "m4a"],
    help="Supported formats: WAV, MP3, M4A"
)

# Process Now when file is upload
if audio_file is not None:

    # show your audio player
    st.audio(audio_file)

    # Process button
    if st.button("🚀 Process Now", type="primary"):

        # Step 1 - Transcribe
        with st.spinner("🎧 Listening to audio..."):

            #  create Temp file 
            suffix = "." + audio_file.name.split(".")[-1]
            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as tmp:
                tmp.write(audio_file.read())
                tmp_path = tmp.name

            # do Transcribe 
            transcribed_text = transcribe_audio(tmp_path)

            #  delete Temp file
            os.unlink(tmp_path)

        # Show Transcription 
        st.markdown("### 📝 Transcribed Text")
        st.success(transcribed_text)

        # Step 2 - detect Intent
        with st.spinner("🧠 Understanding intent..."):
            intent = detect_intent(transcribed_text)

        # Show Intent 
        st.markdown("### 🎯 Detected Intent")

        # Colour according to Intent 
        if intent == "create_file":
            st.info(f"📄 Intent: **{intent}**")
        elif intent == "write_code":
            st.warning(f"💻 Intent: **{intent}**")
        elif intent == "summarize":
            st.success(f"📋 Intent: **{intent}**")
        else:
            st.info(f"💬 Intent: **{intent}**")

        # Step 3 - Execute 
        st.markdown("### ⚡ Action aur Result")

        with st.spinner("🔧 Executing action..."):

            # According to Intent call the tool 
            if intent == "create_file":
                result = create_file(transcribed_text)
                st.success(f"✅ {result}")

            elif intent == "write_code":
                code, filepath = write_code(transcribed_text)

                if filepath:
                    st.success(f"✅ Code file has been saved: {filepath}")
                    st.markdown("**Generated Code:**")
                    st.code(code, language="python")
                else:
                    st.error(code)

            elif intent == "summarize":
                summary = summarize(transcribed_text)
                st.success("✅ Summary is ready!")
                st.markdown("**Summary:**")
                st.write(summary)

            elif intent == "general_chat":
                reply = general_chat(transcribed_text)
                st.success("✅ Response is ready!")
                st.markdown("**Response:**")
                st.write(reply)

        st.markdown("---")
        st.balloons()
        st.success("🎉 Task completed successfully!")

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

    #  Show the Output folder files 
    output_files = os.listdir("output/") if os.path.exists("output/") else []
    if output_files:
        for f in output_files:
            st.text(f"📄 {f}")
    else:
        st.text("No files yet")