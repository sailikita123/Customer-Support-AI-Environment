from fastapi import FastAPI
from inference import run_inference

app = FastAPI()

def main():
    return app

@app.get("/")
def home():
    return {"message": "Customer Support AI Running 🚀"}

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.post("/step")
def step():
    result = run_inference()
    return {"result": result}

@app.get("/health")
def health():
    return {"status": "OK"}
