# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir flask flask_sqlalchemy flask_cors psycopg2-binary

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for SQLAlchemy URI (optional)
# ENV DATABASE_URI="sqlite:///messages.db

# Run the application
CMD ["python", "main.py"]