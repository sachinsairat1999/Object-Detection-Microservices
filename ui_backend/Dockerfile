FROM python:3.8-slim
WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the service port
EXPOSE 8000

# Use Gunicorn to run the Flask app in production
CMD ["gunicorn", "-w", "4", "app:app", "--bind", "0.0.0.0:8000"]
