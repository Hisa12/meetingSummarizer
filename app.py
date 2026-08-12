import streamlit as st
from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#create folder if not exists
Path("uploads").mkdir(exist_ok=True)

st.title("Meeting App")
st.write("Uploading a meeting records")

uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

if uploaded_file:
    # Save the uploaded file to the uploads folder
    file_path = Path("uploads") / uploaded_file.name
    #w = write, b = binary (mp3 is a binary file)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File {uploaded_file.name} uploaded successfully!")

    
    # Now transcribe the audio file
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )


    #create folder if not exists
    Path("transcripts").mkdir(exist_ok=True)

    #Create a text file path
    # Save the uploaded file to the uploads folder
    transcript_file_path = Path("transcripts") / f"{uploaded_file.name}.txt"
    with open(transcript_file_path, "w", encoding="utf-8") as f:
        f.write(transcript.text)

    st.success(f"Transcript saved successfully!")

    st.subheader("Transcript")
    st.text_area("Transcript", value=transcript.text, height=300)


    if st.button("Generate Meeting Summary"):
        st.write("Generating meeting summary...")

        summary = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", 
                 "content": (
                     "You are a helpful assistant that summarizes meeting transcripts."
                     )},
                {"role": "user", 
                 "content": f"""Please summarize this meeting transcript.
                    Please analyze this meeting transcript.

                    Return:

                    1. Summary
                    2. Key Discussion Points
                    3. Action Items
                    4. Decisions

                    Transcript:
                    {transcript.text}
                    """
                }
            ],
        )
        st.subheader("Meeting Summary")
        st.write(summary.choices[0].message.content)
