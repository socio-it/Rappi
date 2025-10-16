from fastapi import FastAPI
from app.mcp.tools import router as mcp_router
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="FastAPI + MCP", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o restringe a ["https://miapp.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye las rutas del MCP
app.include_router(mcp_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
