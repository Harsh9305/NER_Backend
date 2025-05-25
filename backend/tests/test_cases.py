from backend.core.hybrid_extractor import extract_entities
from backend.core.context_resolver import resolve_context
from backend.core.output_formatter import generate_output

def test_full_pipeline():
    input_text = "Configure DUT with User Side VSI with VLAN 100 on Line1"
    entities = extract_entities(input_text)
    resolved = resolve_context(entities)
    output = generate_output(resolved)
    print(output)

if __name__ == '__main__':
    test_full_pipeline()