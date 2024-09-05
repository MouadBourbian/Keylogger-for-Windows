# Logging Server

The logging server receives the keystrokes sent by the keylogger and stores them in a file. It is powered by Docker and Nginx and consists of a Flask-based server that writes the received data into a log file.

## Setup

### 1. Prepare the Docker Environment

Make sure Docker and Docker Compose are installed on your system.

### 2. Start the Server

1. Navigate to the `/logging-server/` directory.
2. Start the server using Docker Compose:

   ```bash
   docker-compose up --build
   ```

   This will start the required containers for the logging server and the Nginx proxy.

3. The logs will be stored in the `/logging-server/logs/` directory.

### 3. Configuration

The Nginx configuration for the proxy pass is defined in the [nginx.conf](./nginx.conf) file. By default, the server listens on port 80 for incoming requests.

## License

This project is licensed under the MIT License. See [LICENSE](../LICENSE) for more details.
