# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10-slim

RUN apt update && apt install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Youtube scripts
COPY ./ /lib/youtube
WORKDIR /lib/youtube

# Install OpenAI Whisper
RUN python3 -m pip install -r requirements.txt

# Expose a PORT to access the python application
EXPOSE $PORT

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 yt:app

# docker buildx build --platform linux/amd64 -t TAG_NAME .