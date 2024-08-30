# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install inotify-tools and rsync
#RUN apt-get update && apt-get install -y inotify-tools rsync

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 8000 for the application
EXPOSE 8000

#RUN chmod +x /app/watch_and_sync.sh
# Collect static files
RUN python3 manage.py collectstatic --noinput
# Run the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "thanhdevops.wsgi:application"]
#CMD ["/bin/bash", "-c", "/app/watch_and_sync.sh & gunicorn --bind 0.0.0.0:8000 thanhdevops.wsgi:application"]
