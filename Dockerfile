FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app
# COPY ./api /app
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]