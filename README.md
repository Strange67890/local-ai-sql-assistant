# 🤖 AI-Powered SQL Assistant (Text-to-SQL)

An intelligent database assistant that converts natural language questions into SQL queries, executes them on a live database, and returns the results. Built with **Python**, **LangChain**, and **Ollama (Llama 3)** for 100% local, privacy-preserving inference.

## 🚀 Features
- **Natural Language Interface:** Ask questions in plain English (e.g., *"Who is the highest rated vendor?"*).
- **Local Inference:** Uses **Llama 3** locally via Ollama—no cloud API keys or costs required.
- **SQL Sanitization:** Automatically detects and strips markdown formatting from generated queries.
- **Direct Database Execution:** Safely connects to MySQL to fetch real-time analytics.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Meta Llama 3 (via Ollama)
- **Orchestration:** LangChain
- **Database:** MySQL
- **Tools:** VS Code, Git

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/text-to-sql-ai.git](https://github.com/YOUR-USERNAME/text-to-sql-ai.git)
   cd text-to-sql-ai