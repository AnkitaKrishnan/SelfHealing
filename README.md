# SelfHealing
Self healing recommendor to recommend Knowledge articles to real time incidents getting generated
# Incident Similarity API

This project provides an API to find the most similar knowledge base (KB) articles for a given incident description. The similarity is calculated using pre-generated embeddings from a SentenceTransformer model.

## Project Structure

kb_incident_project/
│
├── app.py
├── requirements.txt
├── startup.sh
├── data/
│ ├── kb_data.csv
│ └── incident_data.csv
├── utils.py
├── generate_embeddings.py
└── kb_embeddings.pkl


## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip
- Virtual environment (optional but recommended)

### Step 1: Create and Activate Virtual Environment

#### On Windows
```sh
python -m venv venv
venv\Scripts\activate
```
#### On mac
```sh
python -m venv venv
source venv/bin/activate
python generate_embeddings.py
python app.py
```

use curl to see output:
curl -X POST http://127.0.0.1:5000/get_kb -H "Content-Type: application/json" -d '{"incident_number": "INC005", "description": "Users are unable to authenticate due to login issues"}'

