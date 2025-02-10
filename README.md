# 📧 Cold Email Generator

## Overview
Cold Email Generator is a Streamlit-based application that automates personalized cold email creation for business development. By leveraging Groq, LangChain, and ChromaDB, the tool extracts job postings from a company's careers page, analyzes job descriptions, and generates tailored emails with relevant portfolio links.

## Features
- Scrapes job listings from career pages using `WebBaseLoader`.
- Extracts key job details (role, skills, experience, description) using `LangChain`.
- Matches job requirements with relevant projects stored in a vector database (`ChromaDB`).
- Generates personalized cold emails using `ChatGroq`.
- Interactive web interface built with `Streamlit`.

## Tech Stack
- **Python** (Primary language)
- **Streamlit** (Frontend UI)
- **LangChain** (Text processing and LLM integration)
- **Groq (ChatGroq)** (LLM for text generation)
- **ChromaDB** (Vector database for portfolio retrieval)
- **Pandas** (Data handling)
- **dotenv** (Environment variable management)

## Usage
1. **Run the application**:
   ```sh
   streamlit run app.py
   ```
2. **Enter a job listing URL** in the text input field and click "Submit".
3. The tool will:
   - Scrape job listings.
   - Extract relevant job details.
   - Retrieve matching portfolio links.
   - Generate a personalized cold email.
4. **Copy the generated email** and use it for outreach.

## File Structure
```
├── app.py                # Main Streamlit app
├── chains.py             # Handles job extraction & email generation
├── portfolio.py          # Portfolio data handling using ChromaDB
├── utils.py              # Utility functions for text cleaning
├── requirements.txt      # Required dependencies
├── .env                  # Environment variables (not committed)
├── README.md             # Project documentation
```

## Contributing
Feel free to submit issues and pull requests to improve the project.

