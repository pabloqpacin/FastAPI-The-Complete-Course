FROM python:3.12-slim-bullseye

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update && \
#     apt-get install -y vim && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Descomentar y montar la app aquí en la imagen, no en el contenedor( docker-compose.yaml)
# COPY ./src .
COPY ./alembic ./alembic
COPY ./alembic.ini .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["fastapi", "dev", "/app/src/main.py", "--host", "0.0.0.0", "--port", "80"]
# CMD ["fastapi", "run", "/app/src/main.py", "--proxy-headers", "--port", "80"]

