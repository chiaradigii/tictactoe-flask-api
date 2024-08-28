# Tic-Tac-Toe API Technical Documentation

**Author**: Chiara Di Giannantonio

## Overview

This document provides a detailed explanation of the decisions and technologies employed in building the Tic-Tac-Toe API project. It also outlines the branch strategy used during development.

## Table of Contents

1. [Architecture and Design Decisions](#architecture-and-design-decisions)
2. [Technologies Used](#technologies-used)
3. [Branch Strategy](#branch-strategy)
4. [Assumptions](#assumptions)

## Architecture and Design Decisions

### Clean Architecture

The project follows the principles of Clean Architecture, ensuring a clear separation of concerns between different parts of the application:

- **Models**: Business logic and data models are isolated in `models.py`.
- **Routes**: The API endpoints are defined in `routes.py`, keeping them separate from the application setup and business logic.
- **Configuration**: All configurations are managed centrally in `config.py` and pulled from environment variables, making the application easily configurable across different environments.

### 12-Factor App

The project adheres to the 12-Factor App principles, which are crucial for building scalable, maintainable, and cloud-native applications:

- **Configuration Management**: All configurations are stored in environment variables, ensuring that the application can be easily adapted to different environments without code changes.
- **Logging**: Logs are treated as event streams and are output to `stdout`, allowing them to be captured by any logging system.
- **Statelessness**: The application is designed to be stateless, with no session information stored on the server, making it scalable horizontally.

## Technologies Used

### Flask

Flask was chosen for its simplicity and flexibility in building RESTful APIs. It allows for quick development while being powerful enough to handle more complex requirements.

### SQLAlchemy

SQLAlchemy is used as the ORM (Object-Relational Mapper) for managing the database. It simplifies database interactions by providing a high-level abstraction layer.

### Gunicorn

Gunicorn is employed as the WSGI server for running the Flask application in production. It enables the application to handle multiple concurrent requests by running multiple worker processes.

### Docker

Docker is used for containerization, ensuring that the application can be deployed consistently across different environments. It encapsulates the application and its dependencies in a container, making it portable and scalable.

### Logging

Logging is implemented using Python’s built-in `logging` module. Logs are streamed to `stdout` and can be easily configured using environment variables to adjust the verbosity.

## Branch Strategy

The project follows a feature branch strategy, where each new feature or fix is developed in its own branch before being merged into the main branch. This approach helps to keep the main branch stable and allows for parallel development.

### Branch Workflow

1. **Main Branch (`main`)**: The main branch holds the stable version of the code. It is protected and only receives updates through pull requests.
   
2. **Feature Branches**: Each feature or bug fix is developed in a separate branch:
    - **Naming Convention**: Branches are named using the format `feature/<feature-name>`

3. **Pull Requests**: Once a feature is complete, a pull request is created to merge the feature branch into the main branch. The pull request includes a description of the changes and is reviewed before merging.

4. **Testing**: Unit tests are added for each feature, ensuring that new code is properly tested before being integrated into the main branch.

### Continuous Integration (CI)

To further enhance the branch strategy, a CI pipeline could be introduced to automatically run tests on each pull request, ensuring that code quality is maintained and reducing the risk of introducing bugs into the main branch.

## Assumptions

### Scalability Requirements

The project assumes that the application will need to scale horizontally, leading to decisions like using Gunicorn and Docker for managing concurrency and deployment.

### Configuration Flexibility

It was assumed that the application would be deployed across different environments (development, staging, production), so configurations are managed through environment variables.

### Logging

The need for robust monitoring and observability guided the decision to implement comprehensive logging throughout the application, adhering to the 12-Factor App principles.
