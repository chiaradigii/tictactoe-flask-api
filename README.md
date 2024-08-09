# Tic-Tac-Toe API
This project implements a RESTful API for a Tic-Tac-Toe game using Flask. The API allows users to create new games, make moves, and check the status of ongoing games. The project is designed with scalability, observability, and configurability in mind.

## Table of Contents

1. [Deployment](#deployment)
2. [Configuration](#configuration)
3. [Execution](#execution)

## Deployment

### Prerequisites

- **Python 3.8+**: Ensure that Python is installed on your system.
- **Docker** (optional but recommended): For containerized deployment.
- **Gunicorn**: Used as the WSGI server to run the Flask application.

### Local Deployment

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/tictactoe-flask-api.git
    cd tictactoe-flask-api
    ```

2. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file at the root of the project with the following content:
      ```plaintext
      FLASK_ENV=development
      SECRET_KEY=your_secret_key
      SQLALCHEMY_DATABASE_URI=sqlite:///tic_tac_toe.db
      LOG_LEVEL=DEBUG
      PORT=3100
      ```

5. **Run the Migrations**:
    ```bash
    flask db upgrade
    ```

### Docker Deployment

1. **Build the Docker Image**:
    ```bash
    docker build -t tictactoe-api .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -d -p 3100:3100 tictactoe-api
    ```

## Configuration

### Environment Variables

The application uses environment variables to manage configurations. Here are the key variables:

- **`FLASK_ENV`**: Specifies the environment (development, production).
- **`SECRET_KEY`**: Used by Flask for session management.
- **`SQLALCHEMY_DATABASE_URI`**: The database connection string.
- **`LOG_LEVEL`**: Defines the logging level (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- **`PORT`**: The port on which the application listens.

### Configuration Files

- **`config.py`**: Contains the configuration classes for different environments (development, production).
- **`gunicorn.conf.py`**: Configures Gunicorn for handling concurrency and port binding.

## Execution

### Running the Service Locally

1. **Start the Flask Application**:
    ```bash
    flask run
    ```

2. **Running with Gunicorn**:
    ```bash
    gunicorn -c app/gunicorn.conf.py -b 0.0.0.0:${PORT:-3100} app:app
    ```

### Running the Service in Docker

- Once the Docker container is running, the service will be accessible at `http://localhost:3100`.

