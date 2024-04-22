# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Ensure this dockerfile in directory of project
WORKDIR /

# Set the working directory to the dir we created above
COPY . /

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# # Run flask app on port 5000 first = host machine, second = flask of docker container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "app.py"]