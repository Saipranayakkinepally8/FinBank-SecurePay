from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fin Bank Secure Pay API is running"}
