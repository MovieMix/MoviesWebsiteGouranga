# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /MoviesApp

# Copy the application files into the working directory
COPY . /MoviesApp

# Install the application dependencies
RUN pip install -r requirements.txt

# Set the health check command
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000