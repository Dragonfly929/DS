# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the service
EXPOSE 5000

# Run the User and Palette Management Service
CMD ["python", "app.py"]
