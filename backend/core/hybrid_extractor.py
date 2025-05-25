from backend.models.ner_model import load_ner_model
from backend.rules.entity_ruler import add_entity_ruler

def extract_entities(text):
    nlp = load_ner_model()
    nlp = add_entity_ruler(nlp)
    doc = nlp(text)
    return {ent.label_: ent.text for ent in doc.ents}