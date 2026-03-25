# 📓 DevDiary - AI-Powered Smart Notepad

DevDiary is a full-stack personal tool that records daily notes during software development processes, analyzes these notes using a local LLM (Large Language Model), and automatically generates weekly Markdown reports.

## 🚀 Features

- **Local AI Integration:** Notes are analyzed using the Ollama (Llama 3.2) model running locally on your machine, without the need for any external APIs (e.g., OpenAI).
- **RESTful API:** A fast and modern backend architecture built with FastAPI, handling all CRUD operations.
- **Persistent Data Storage:** Efficient data management on SQLite using SQLAlchemy ORM.
- **Automated Reporting:** A scheduled automation script (via Cron Job or Windows Task Scheduler) that reads notes from the database and generates elegant weekly Markdown (`.md`) reports.
- **Lightweight UI:** A minimalist web interface written in Vanilla JavaScript and HTML/CSS, fully integrated with the API using the Fetch API.

## 🛠️ Technologies Used

- **Backend:** Python 3, FastAPI, Uvicorn
- **Database:** SQLite, SQLAlchemy, Pydantic (Data Validation)
- **Artificial Intelligence:** Ollama, Llama 3.2 (Local LLM)
- **Frontend:** HTML5, CSS3, Vanilla JS

## ⚙️ Setup and Execution

### 1. Prerequisites
- [Python 3.x](https://www.python.org/) must be installed on your system.
- [Ollama](https://ollama.com/) must be installed with the **Llama 3.2** model downloaded for local AI analysis:
  ```bash
  ollama run llama3.2
  ```

### 2. Cloning the Repository and Installation
Clone the project to your local machine and install the dependencies:

```bash
git clone [https://github.com/Safa67/devdiary.git](https://github.com/Safa67/devdiary.git)
cd devdiary

# Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install required packages
pip install fastapi uvicorn sqlalchemy pydantic requests
```

### 3. Running the Application

**Step 1: Start the FastAPI Server**
```bash
uvicorn main:app --reload
```
*The API server will be available at `http://127.0.0.1:8000`. You can access the interactive API documentation at `/docs`.*

**Step 2: Start the Frontend Interface**
Open a new terminal window and start a local HTTP server to avoid CORS issues:
```bash
python -m http.server 5500
```
*Navigate to `http://localhost:5500` in your web browser to start using the application.*

## 📅 Automation (Weekly Reporting)

The `reporter.py` script located in the project directory reads all notes and AI analyses from the database and generates a `.md` file stamped with the current date.

To test it manually:
```bash
python reporter.py
```
*This script is designed to be automated using a Linux Cron Job or Windows Task Scheduler (e.g., set to run every Friday at 17:00).*
