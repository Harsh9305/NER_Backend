from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.core.hybrid_extractor import extract_entities
from backend.core.context_resolver import resolve_context
from backend.core.output_formatter import generate_output

router = APIRouter()

class TestProcedureInput(BaseModel):
    text: str

@router.post("/extract")
def parse_test_procedure(payload: TestProcedureInput):
    try:
        entities = extract_entities(payload.text)
        resolved = resolve_context(entities)
        output = generate_output(resolved)
        return {"entities": resolved, "formatted_output": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))