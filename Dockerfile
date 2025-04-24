#  base image
FROM python:3.13-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy rest of the app
COPY . .

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
