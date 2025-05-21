# 🔍 RAG Multidomain Demo

This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using LangChain, FAISS, and 
OpenAI's language models.

We use a public PDF on Python programming ([URL](https://www.halvorsen.blog/documents/programming/python/resources/Python%20Programming.pdf)) 
as our document source, and process it through chunking, embedding, 
and vector search to answer questions via an LLM.

---

## 📦 Features

- ✅ Load and parse a PDF file into LangChain Documents  
- ✂️ Split documents into chunks with context overlap  
- 🧠 Generate vector embeddings using OpenAI  
- 📚 Store vectors in a local FAISS vectorstore  
- ❓ Query the system and retrieve context-aware answers from LLM  

---

## 🛠️ Technologies Used

- Python 3.12  
- LangChain  
- OpenAI GPT models  
- FAISS (in-memory vector database)  
- Jupyter Notebook (optional)  
- Conda (for environment management)  

---

## 📁 Project Structure
```plaintext'
rag-multidomain-demo/
├── data/ # PDF files
├── notebooks/ # Jupyter notebooks 
├── src/
│ ├── embeddings/ # Embedding model loader
│ ├── loaders/ # PDF loader
│ ├── preprocessing/ # Text splitter
│ ├── rag/ # QA chain (retrieval + LLM)
│ ├── vectorstore/ # FAISS DB setup
│ ├── main.py # Full example pipeline
│ └── main_demonstrate.py # Code for better demonstrate all parts (run in CONCOLE)
├── .env # API key (excluded from git)
├── .gitignore
├── _conda_env_name.txt # name for conda enviromnent
├── _conda_install_requirements.bat # bash script to install conda env with python version
├── _create_conda_env.bat # bash script to install requirements into conda env
├── README.md # markdown readme document
└── requirements.txt # list od requirement - python libraries
```
---

## ▶️ Quick Start

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/rag-multidomain-demo.git
cd rag-multidomain-demo
```
2 **Create conda env**
```bash
_create_conda_env.bat
```
3. **Install requirements**
```bash
_conda_install_requirements.bat
```

---

## Create a file .env and add up your OpenAI API key:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Run the main pipeline
```bash
python main.py
```