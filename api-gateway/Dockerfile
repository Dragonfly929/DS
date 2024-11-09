# Use Python 3.9 slim base image (specific version for consistency)
FROM python:3.9.12-slim

# Set working directory in the container
WORKDIR /app

# Copy the necessary files for the application
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on (change to your desired port if necessary)
EXPOSE 8080

# Set the entry point to run the API Gateway (main.py)
CMD ["python", "main.py"]
