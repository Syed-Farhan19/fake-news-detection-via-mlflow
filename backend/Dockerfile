FROM python:3.11-slim

WORKDIR /app

# Only copy requirements first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend files (excluding ignored ones)
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
