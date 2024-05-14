FROM python:3.9.19-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -yqq \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
