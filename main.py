from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# initialize FastAPI app
app = FastAPI(
    title="Text CLassification API",
    description="Classify text using Huggingface Transformers",
    version="1.0"
)

# Load Huggingface Transformer Model (e.g - DistilBERT for sentiment analysis)
classifier = pipeline("sentiment-analysis")

# Define Request Body
class TextInput(BaseModel):
    text: str
    
# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to Text CLassification API"
    }
    
# Text classification Endpoint
@app.post("/classify/")
def classify_text(input_data: TextInput):
    try:
        result = classifier(input_data.text)[0]
        return {
            "label": result['label'],
            "confidence": round(result['score'], 4)
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
# Health Check Endpoint
@app.get("/health")
def health_check():
    return {
        "status":"healthy"
    }