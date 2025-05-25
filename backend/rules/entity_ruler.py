import spacy
import json
from pathlib import Path

def add_entity_ruler(nlp):
    ruler = nlp.add_pipe("entity_ruler", before="ner")
    patterns_path = Path("backend/data/patterns.jsonl")
    with patterns_path.open("r") as f:
        patterns = [json.loads(line) for line in f]
    ruler.add_patterns(patterns)
    return nlp