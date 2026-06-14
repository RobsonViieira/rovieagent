from fastapi import FastAPI

app = FastAPI(title="RovieAgent", version="0.1.0")

@app.get("/")
async def root():
    return {"name": "RovieAgent", "version": "0.1.0", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/api/v1/agents")
async def agents():
    return {"agents": [
        {"id": "research", "name": "Research Agent", "status": "available"},
        {"id": "content", "name": "Content Agent", "status": "available"},
        {"id": "code", "name": "Code Agent", "status": "available"}
    ]}
