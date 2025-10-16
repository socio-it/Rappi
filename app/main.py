from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.mcp.tools import mcp_app

app = FastAPI(title="FastAPI + MCP (SSE)", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta el servidor MCP real en /mcp
app.mount("/mcp", mcp_app)

@app.get("/health")
def health():
    return {"status": "ok"}
