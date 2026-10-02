from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.analyze import router as analyze_router

app = FastAPI(title="ProblemPool API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze_router, prefix="/api")

@app.get("/")
def root():
    return {"name": "ProblemPool API", "status": "ok", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}
