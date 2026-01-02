# 🎟️ Universal Video Scanner

Universal Video Scanner with Web Interface - Automatic detection of HDR formats including Dolby Vision enhancement layers in video files.

## Features ✨

- **Automatic Scanning**: Watchdog-based detection of new media files
- **All HDR Formats**: SDR, HDR10, HDR10+, HLG, and Dolby Vision (all profiles)
- **Dolby Vision Analysis**: Detection of MEL (Minimum Enhancement Layer) and FEL (Full Enhancement Layer) for all Dolby Vision profiles
- **Web Interface**: Modern dark-theme dashboard on port 2367
- **dovi_tool Integration**: Complete RPU analysis and enhancement layer detection
- **Docker-based**: Simple deployment with Docker Compose
- **Manual Scan**: Fallback button for on-demand scanning

## Software on Docker Hub 🐳

The software is also available on [Docker Hub](https://hub.docker.com/r/u3known/universal-video-scanner/):

![Docker Hub](https://www.docker.com/wp-content/uploads/2023/05/Moby-logo.png)

## Quick Start 🚀

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
```bash
git clone https://github.com/U3knOwn/universal-video-scanner.git
cd universal-video-scanner
```

2. Create media directory:
```bash
mkdir -p media
```

3. Start container:
```bash
docker-compose up -d
```

4. Open web interface:
```
http://localhost:2367
```

## Usage 📖