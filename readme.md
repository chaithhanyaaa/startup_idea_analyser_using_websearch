# 🚀 Startup Insight AI

An AI-powered startup idea validation tool that combines **live web research** with a **Large Language Model (LLM)** to generate a detailed business analysis.

The application researches the startup idea using **Tavily Search**, enriches the prompt with current market information, and leverages **Ollama + LangChain** to provide structured insights including competitors, market opportunities, risks, monetization strategies, and an overall startup score.


---

## ✨ Features

- 🔍 Live web research using Tavily Search API
- 🤖 AI-powered startup analysis using Ollama
- 🏢 Competitor identification
- 📈 Market opportunity analysis
- 💪 Strengths & Weaknesses
- ⚠️ Risk assessment
- 💰 Monetization strategy suggestions
- 🛠️ MVP feature recommendations
- ⭐ Overall startup score
- 🎨 Modern Streamlit interface

---

## 🏗️ System Architecture

```text
                 User Startup Idea
                         │
                         ▼
               Tavily Web Search
                         │
                         ▼
               Research Context
                         │
                         ▼
             LangChain Prompt Template
                         │
                         ▼
                 Ollama (Qwen Model)
                         │
                         ▼
            Pydantic Output Parser
                         │
                         ▼
                Structured Analysis
                         │
                         ▼
                  Streamlit Dashboard
```

---

## 📂 Project Structure

```text
startup-insight-ai/

│── app.py                 # Streamlit UI
│── chain.py               # Orchestrates the workflow
│── llm.py                 # Ollama model configuration
│── prompt.py              # Prompt templates
│── websearch.py           # Tavily Search integration
│── requirements.txt
│── .env
└── README.md
```

---

## ⚙️ Tech Stack

### AI

- LangChain
- Ollama
- Qwen Model
- Tavily Search API

### Backend

- Python
- Pydantic

### Frontend

- Streamlit

### Tools

- dotenv
- Git
- GitHub

---

## 🔄 Workflow

1. User enters a startup idea.
2. Tavily searches the web for relevant information.
3. Search results are added to the prompt.
4. LangChain sends the enriched prompt to the LLM.
5. The model returns a structured business analysis.
6. Pydantic validates the output.
7. Streamlit displays the final report.

---

## 📊 Analysis Generated

The application provides:

- Executive Summary
- Competitor Analysis
- Market Opportunity
- Strengths
- Weaknesses
- Risks
- Monetization Strategy
- MVP Recommendations
- Overall Startup Score
- Final Recommendation

---

## 🧠 What I Learned

Through this project I learned:

- Designing AI applications with modular architecture
- Building LangChain pipelines
- Prompt engineering
- Integrating external tools with LLMs
- Using Pydantic for structured outputs
- Working with local LLMs using Ollama
- Error handling and validation
- Streamlit application development

---

## 🚀 Installation

Clone the repository

```bash
git clone <your-repository-url>
```

Move into the project

```bash
cd startup-insight-ai
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
TAVILY_API_KEY=your_api_key_here
```

Run the application

```bash
streamlit run app.py
```

---

## 💡 Future Improvements

- Multi-Agent Architecture
- Memory Support
- Chat-based Startup Advisor
- PDF Report Generation
- Investment Readiness Score
- Pitch Deck Generator
- Startup Idea Comparison
- Multi-LLM Support (OpenAI, Gemini, Claude)
- Docker Deployment

---

## ⭐ Why This Project?

Instead of relying solely on an LLM's internal knowledge, this project enhances responses using **live web research**, enabling more relevant and up-to-date startup analysis.

The architecture follows a modular design where each component has a single responsibility, making the application easy to maintain and extend.

---

## 📬 Connect with Me

If you have suggestions or feedback, feel free to connect!

- LinkedIn: *(Add your LinkedIn)*
- GitHub: *(Add your GitHub)*

---

If you found this project interesting, consider giving it a ⭐ on GitHub!