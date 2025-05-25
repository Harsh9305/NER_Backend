# NLP Backend Parser for Test Procedures

## 🚀 Setup & Run

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Generate training data
```bash
python backend/data/training_data.spacy
```

### Step 3: Train the spaCy model
```bash
python -m spacy init config config.cfg --lang en --pipeline ner
python -m spacy train config.cfg --output backend/models/ --paths.train backend/data/training_data.spacy --paths.dev backend/data/training_data.spacy
```

### Step 4: Start the backend
```bash
uvicorn backend.app:app --reload
```

### Step 5: Test the API
POST http://127.0.0.1:8000/extract
Body:
```json
{
  "text": "Configure DUT with User Side VSI with VLAN 100 on Line1"
}
```