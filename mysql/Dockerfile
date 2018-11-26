# Use an official Python runtime as a parent image
FROM mysql

# Set the working directory to /app
WORKDIR 

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get install default-libmysqlclient-dev

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
#ENV 

# Run app.py when the container launches
CMD ["python3", "app.py"]
