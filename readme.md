
# 🎥 Phi Multi-Modal AI Agent: Video Summarizer & Analyzer  
Powered by **Google Gemini AI** + **DuckDuckGo Search** + **Streamlit**  

An AI-powered application that summarizes and analyzes video content using Google's Gemini AI model. This tool allows users to upload videos, ask contextual questions, and receive comprehensive AI-generated insights enhanced by real-time web research and RAG to fetch data.

## 🚀 Features  
- 📂 **Upload Video Files** (`mp4`, `mov`, `avi`)  
- 🤖 **Gemini AI-Powered Analysis & Summarization**  
- 🌐 **Web Search Integration via DuckDuckGo** for supplementary information  
- ⏱️ **Real-Time AI Processing with User-Friendly Interface**  
- 🧠 **Multi-Modal Agent** support for querying and interactive responses  
- 💡 **Custom Query Input** for deep video content analysis  
- 🔐 **Secure API Key Handling** via `.env` file  
- 🔥 Built with **Streamlit** for an interactive web interface  

---

## 📸 Demo  
![App Screenshot]("asset\Screenshot 2025-03-21 150245.png")
![App Screenshot]("asset\Screenshot 2025-03-21 150334.png")
---

## 🏗️ Tech Stack  
- [Streamlit](https://streamlit.io/) - UI and Interaction  
- [Google Gemini AI](https://deepmind.google/) - Language & Vision Analysis     
- [DuckDuckGo Search Tool](https://duckduckgo.com/) - Web Search Enhancer  
- [phi-agent](https://pypi.org/project/phi/) - Multi-Agent Orchestration  
- Python 3.9+

---

## 🛠️ Setup Instructions  

### 1. Clone the repository  
```bash
git clone https://github.com/Ram2049/Video_summerizer
cd Video_summerizer
```

### 2. Install dependencies  
We recommend using a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your API Key to `.env`  
Create a `.env` file in the root directory with the following:  
```
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 4. Run the app  
```bash
streamlit run app.py
```

---

## 📁