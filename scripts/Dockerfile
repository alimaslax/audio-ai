FROM alpine:3.17

# Install development tools for C++ and Bash
RUN apk add --update \
    build-base \
    cmake \
    gcc \
    g++ \
    bash \
    && rm -rf /var/cache/apk/*

# Set the working directory
WORKDIR /app

# Copy the source code to the container
COPY ./source .

COPY ./lex.wav ./lex.wav
# Compile the code
RUN cmake . && make

# Set the entrypoint to Bash
ENTRYPOINT ["/app/bin/main", "-f", "/app/lex.wav"]