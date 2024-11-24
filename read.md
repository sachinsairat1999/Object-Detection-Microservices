# Object Detection 

This project consists of two services: a UI backend and an AI backend.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo
    cd object-detection-microservice
    ```

2. Build and run both services using Docker Compose:
    ```bash
    docker-compose up --build
    ```

The UI service will be available on `http://localhost:5000` and the AI service will be available on `http://localhost:5001`.

## Usage

- Upload an image through the UI to perform object detection.
- The results will be returned and displayed in JSON format.
