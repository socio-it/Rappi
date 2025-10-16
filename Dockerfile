
FROM python:3.11-slim AS builder

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


FROM python:3.11-slim


ENV PYTHONUNBUFFERED=1
WORKDIR /app


COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH


COPY . .

# Puerto interno para Traefik
EXPOSE 8000

# Comando para ejecutar FastAPI con Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
