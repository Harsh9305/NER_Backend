# 🧠 NLP Backend Parser for Test Procedures

This backend system extracts configuration entities from natural language test procedures (like Nokia use cases) using a hybrid NLP approach (ML + rule-based).

---

## ⚙️ Setup & Run

### ✅ Step 1: Create Virtual Environment
```bash
python -m venv venv
```

### ✅ Step 2: Activate Environment

- **Windows**
  ```bash
  venv\Scripts\activate
  ```

- **Linux/Mac**
  ```bash
  source venv/bin/activate
  ```

---

### 📦 Step 3: Install Requirements
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

### 🧪 Step 4: Generate Training Data

First, rename the script:
```
backend/data/training_data.spacy ➜ backend/data/generate_training_data.py
```

Then run:
```bash
python backend/data/generate_training_data.py
```

This will create:
```
backend/data/training_data.spacy
```

---

### 🧠 Step 5: Train the spaCy NER Model
If you already downloaded `config.cfg` from earlier, use it directly:
```bash
python -m spacy train config.cfg --output backend/models/ \
  --paths.train backend/data/training_data.spacy \
  --paths.dev backend/data/training_data.spacy
```

---

### 🚀 Step 6: Start the Backend Server
```bash
uvicorn backend.app:app --reload
```

This will start the FastAPI server on:
```
http://127.0.0.1:8000
```

---

## 📬 Step 7: Submit Test Procedure

### Endpoint:
```
POST http://127.0.0.1:8000/extract
```

### Example Body:
```json
{
  "text": "Configure DUT with User Side VSI with VLAN 100 on Line1"
}
```

### Sample Response:
```json
{
  "entities": {
    "VLAN": "100",
    "LINE": "Line1",
    "FORWARDER": "N:1"
  },
  "formatted_output": "Entity1 = DUT\nEntity1 Keywords =\nUserVSI-1 = VLAN=100, PBIT=0\nUserVSI-1 Parent = Line1\nForwarder = N:1"
}
```
