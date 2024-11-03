FROM python:3

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi
RUN pip install fastapi uvicorn

WORKDIR /app

COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port", "80"]