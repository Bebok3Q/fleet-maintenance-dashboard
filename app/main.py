from fastapi import FastAPI
from .db import engine, Base
from .routes import vehicles, diagnostics, maintenance

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(vehicles.router, prefix="/api", tags=["Vehicles"])
app.include_router(diagnostics.router, prefix="/api", tags=["Diagnostics"])
app.include_router(maintenance.router, prefix="/api", tags=["Maintenance"])




@app.get('/')
def read_root():
    return {"message": "Fleet Maintenance API is running."}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

