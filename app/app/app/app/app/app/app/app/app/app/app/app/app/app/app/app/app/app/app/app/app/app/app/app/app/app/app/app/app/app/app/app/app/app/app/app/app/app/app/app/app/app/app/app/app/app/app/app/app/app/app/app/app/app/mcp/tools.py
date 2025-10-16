from fastapi import APIRouter, Query

router = APIRouter(prefix="/mcp", tags=["mcp"])

# --- Endpoint base para comprobar si el MCP está activo ---
@router.get("/ping")
async def ping():
    return {"mcp_status": "alive"}

# --- Herramienta MCP: sumar dos números ---
def mcp_sum(a: float, b: float) -> float:
    """
    Suma dos números y devuelve el resultado.
    """
    return a + b

# --- Endpoint para acceder a la herramienta vía API ---
@router.get("/sum")
async def sum_endpoint(
    a: float = Query(..., description="Primer número"),
    b: float = Query(..., description="Segundo número")
):
    """
    Endpoint que llama a la herramienta MCP de suma.
    """
    result = mcp_sum(a, b)
    return {"a": a, "b": b, "result": result}

__all__ = ["router", "mcp_sum"]
