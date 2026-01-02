# Docker Build Files

This directory contains files required during the Docker build process.

## Required Files

### dovi_tool

The `dovi_tool` binary is required for Dolby Vision analysis.

**Download Instructions:**

```bash
cd files
wget https://github.com/quietvoid/dovi_tool/releases/download/2.3.1/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz
```

This file is automatically excluded from git via `.gitignore` due to its size (2.3 MB).

## Docker Build Process

The Dockerfile will copy these files from this directory during the build process:
- `files/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz` → extracted to `/usr/local/bin/dovi_tool`

## Setup Before Building

Before running `docker-compose up -d --build`, ensure you have downloaded the required file:

```bash
# Download dovi_tool if not already present
if [ ! -f files/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz ]; then
    cd files
    wget https://github.com/quietvoid/dovi_tool/releases/download/2.3.1/dovi_tool-2.3.1-x86_64-unknown-linux-musl.tar.gz
    cd ..
fi

# Build the Docker image
docker-compose up -d --build
```

## Notes

- These files are not included in the repository to keep the repository size small
- The files must be downloaded manually before building the Docker image
- The build process will fail if these files are missing
