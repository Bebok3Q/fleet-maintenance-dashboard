from fastapi import FastAPI
from .db import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get('/')
def read_root():
    return {"message": "Fleet Maintenance API is running."}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

