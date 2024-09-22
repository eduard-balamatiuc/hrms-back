# HRMS Backend
![Tox Check](https://github.com/eduard-balamatiuc/hrms-back/workflows/Tox%20Check/badge.svg)

## Overview

Welcome to the HRMS (Human Resource Management System) Backend project. This is a RESTful backend service developed using FastAPI, intended to manage human resources data, including user authentication, roles, and appointments. The service makes use of PostgreSQL, MongoDB, and Redis for data storage and caching.

## Features

- User registration and authentication
- Role-based access control (Patient, Doctor, Admin)
- Appointment scheduling
- Data validation using Pydantic
- Asynchronous capabilities provided by FastAPI
- Docker support for deployment

## Getting Started

### Prerequisites

Before you begin, ensure you have the following software installed:

- Docker
- Docker Compose
- Python 3.10 (for development)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/hrms-back.git
   cd hrms-back
   ```

2. **Set up environment variables**:

   Create a `.env` file in the root directory and add your configuration for PostgreSQL and other services.

3. **Build and run the Docker containers**:

   ```bash
   docker-compose up --build
   ```

### Running the Application

The application will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

### Running Tests

You can run tests using Tox, which is configured to check code quality and run static analysis tools. Make sure you have Tox installed:

```bash
pip install tox
```

Then run:

```bash
tox
```

## Technologies Used

- **FastAPI**: A modern web framework for building APIs with Python quickly.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **MongoDB**: A NoSQL database designed for scalability and flexibility.
- **Redis**: An in-memory data structure store used for caching and message brokering.
- **Pydantic**: Data validation and settings management using Python type annotations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please create a pull request or open an issue for any enhancements or bugs you may find.

