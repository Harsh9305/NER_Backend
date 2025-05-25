from fastapi import FastAPI
from fastapi.responses import JSONResponse
from backend.api.routes import router

app = FastAPI()
@app.get("/")
def read_root():
    return JSONResponse(content={"message": "✅ NLP Test Procedure Extractor is Running!"})
app.include_router(router)
