# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /FSC_MVP

# Copy the current directory contents into the container at /app 
ADD . /FSC_MVP

# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "uwsgiConfig.ini"]
