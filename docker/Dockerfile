# syntax=docker/dockerfile:1.4

# ==========================
# Étape 1 : Build léger
# ==========================
FROM python:3.11-slim as builder

LABEL maintainer="Altiora Team <contact@altiora.fr>"
LABEL version="2.0.0"
LABEL description="Backend Altiora V2 – FastAPI avec Qwen3 & Starcoder2"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY backend/requirements/base.txt backend/requirements/prod.txt ./
RUN pip install --upgrade pip setuptools wheel && \
    pip install -r prod.txt

# ==========================
# Étape 2 : Image finale
# ==========================
FROM python:3.11-slim as runtime

RUN groupadd -r altiora && useradd -r -g altiora altiora
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
RUN mkdir -p /app/logs /app/data /app/models && \
    chown -R altiora:altiora /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --chown=altiora:altiora backend/altiora ./altiora
COPY --chown=altiora:altiora backend/pyproject.toml ./

RUN pip install -e .

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

USER altiora
CMD ["uvicorn", "altiora.api.app:app", "--host", "0.0.0.0", "--port", "8000"]