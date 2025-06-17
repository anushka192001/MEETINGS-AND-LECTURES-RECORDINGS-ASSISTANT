FROM python:3.11.4-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive PIP_PREFER_BINARY=1

WORKDIR /app

RUN apt update && apt install -y software-properties-common curl ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY src/ /app/src
COPY main.py /app/main.py
COPY requirements.lock /app/requirements.lock
COPY pyproject.toml /app/pyproject.toml
COPY README.md /app/README.md

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.lock

CMD ["python3.11", "main.py"]
