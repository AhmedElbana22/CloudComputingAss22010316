FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Pyth.py random_paragraphs.txt ./

CMD ["python", "Pyth.py"]