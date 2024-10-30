# Use an official lightweight Python image
FROM python:3.9-slim

# Create a non-root user
RUN useradd -m sophnel

# Set the working directory
WORKDIR /home/sophnel/app

# Copy the requirements file and install dependencies
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY url_extractor/url_extractor.py .

# Change ownership to the non-root user
RUN chown -R sophnel:sophnel /home/sophnel/app

# Switch to the non-root user
USER sophnel

# Entry point to pass arguments to the script
ENTRYPOINT ["python3", "url_extractor.py"]