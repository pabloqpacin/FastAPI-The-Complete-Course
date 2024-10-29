FROM python:3.12-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Descomentar y montar la app aquí en la imagen, no en el contenedor( docker-compose.yaml)
# COPY ./app .

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

EXPOSE 80

CMD ["fastapi", "dev", "/app/main.py", "--host", "0.0.0.0", "--port", "80"]
# CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80"]

