from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from deserializer3 import get_risk_instance
from pydantic_model3 import Risk
from logic3 import RiskProcessor  

app = FastAPI()

class AnalyzeRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    # Beispiel: Dummy-Eingabe verarbeiten
    dummy_file = "Third_Version_MR/4risk_example.json"
    risk_instance = get_risk_instance(dummy_file)
    processor = RiskProcessor(risk_instance)
    response_text = processor.process(return_text=True)
    
    return {"response": response_text}

if __name__ == "__main__":
    uvicorn.run("mock_server:app", host="0.0.0.0", port=8000, reload=True)