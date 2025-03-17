FROM python:3.10-slim

WORKDIR /app

# install dependecies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy FastAPI code
COPY . .

# Expose port and run the FastAPI app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]