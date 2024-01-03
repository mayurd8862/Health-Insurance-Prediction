FROM python:3.11.4
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]



# # Use the official Python image as a base image
# FROM python:3.11.4

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY . /app

# # Install any dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the current directory contents into the container at /app
# COPY . /app/

# # Expose the port that Flask will run on
# EXPOSE 5000

# # Set environment variables
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# # Command to run when the container starts
# CMD ["flask", "run"]
