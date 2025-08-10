# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Installera systemberoenden
RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    curl \
    gnupg \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Installera geckodriver
RUN GECKODRIVER_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest \
    | grep "tag_name" | cut -d '"' -f 4) && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz" && \
    tar -xzf "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz" -C /usr/local/bin && \
    rm "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz"


# Set working directory in the container
WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the backend code
COPY . /app

# Start main.py
CMD ["python", "python/main.py"]

