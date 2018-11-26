# Use an official Python runtime as a parent image
FROM python

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get install default-libmysqlclient-dev
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV http_proxy localhost:5000
#ENV https_proxy localhost:5000
#ENV FLASK_APP app.py
#ENV FLASK_DEBUG 1

# Run app.py when the container launches
#CMD ["python3", "app.py"]
