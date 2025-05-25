import spacy

def load_ner_model():
    return spacy.load("backend/models/model-best")