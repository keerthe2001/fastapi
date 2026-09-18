from fastapi import FastAPI

app = FastAPI(title="FastAPI")

@app.get("/")
def read_root():
    return {"Hello": "World"}