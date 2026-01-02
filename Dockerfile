FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    mediainfo \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dovi_tool from local files
COPY files/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz /tmp/
RUN tar -xzf /tmp/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz -C /tmp/ \
    && mv /tmp/dovi_tool /usr/local/bin/ \
    && chmod +x /usr/local/bin/dovi_tool \
    && rm /tmp/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY config.py .
COPY services/ ./services/
COPY utils/ ./utils/
COPY watchers/ ./watchers/

# Create media directory
RUN mkdir -p /media

# Expose port
EXPOSE 2367

# Run the application
CMD ["python3", "app.py"]
