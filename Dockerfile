# Use a base image with Python runtime
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 5000

# Set the entrypoint command to run the Flask application
CMD ["python", "app.py"]

