# 🎙️ AI Meeting Summarizer

An AI-powered meeting summarizer built with Python and Streamlit.

The app allows users to upload a meeting recording, convert the audio into text using OpenAI's speech-to-text API, and generate an AI-powered meeting summary.

## ✨ Features

* 🎙️ Upload meeting audio files
* 📝 Convert audio into a transcript
* 💾 Save audio files locally
* 📄 Save transcripts as text files
* 🤖 Generate AI meeting summaries
* 📌 Extract key discussion points
* ✅ Identify action items
* 💡 Identify important decisions
* 📥 Download meeting results

## 🛠️ Technologies

* **Python**
* **Streamlit** — web interface
* **OpenAI API** — transcription and summarization
* **python-dotenv** — environment variable management
* **Git & GitHub** — version control

## 📂 Project Structure

```text
AIMettingProject/
│
├── app.py
├── .env
├── .gitignore
│
├── uploads/
├── transcripts/
├── reports/
│
└── venv/
```

### Important

The following files/folders are not uploaded to GitHub:

```text
.env
venv/
uploads/
```

The `.env` file contains the OpenAI API key and must remain private.

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hisa12/meetingSummarizer.git
```

### 2. Open the project

```bash
cd meetingSummarizer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install streamlit openai python-dotenv
```

### 6. Create a `.env` file

Create a file named:

```text
.env
```

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

**Never upload your `.env` file to GitHub.**

### 7. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## 🔄 How It Works

```text
Meeting Audio
      ↓
Streamlit Upload
      ↓
Save Audio
      ↓
OpenAI Speech-to-Text
      ↓
Transcript
      ↓
OpenAI GPT
      ↓
Meeting Summary
      ↓
Key Points + Action Items + Decisions
```

## 🎯 Project Goal

This project was created as a two-week beginner Python project to learn:

* Python
* APIs
* Streamlit
* File handling
* Environment variables
* AI integration
* Git and GitHub

## 🔐 Security

Never commit your API key to GitHub.

The `.gitignore` file is used to prevent sensitive files such as `.env` from being uploaded.

## 📌 Project Status

🚧 **Currently in development**

More features and improvements will be added as the project progresses.
