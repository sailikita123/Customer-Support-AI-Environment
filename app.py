from fastapi import FastAPI
from inference import run_inference

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Customer Support AI Running 🚀"}

@app.get("/run")
def run():
    result = run_inference()
    return {
        "status": "success",
        "result": result
    }

@app.get("/health")
def health():
    return {"status": "OK"}


@app.post("/reset")
def reset():
    return {
        "status": "reset successful"
    }



@app.post("/step")
def step():
    result = run_inference()
    return {
        "status": "step executed",
        "result": result
    }