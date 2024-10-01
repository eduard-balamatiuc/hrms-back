# Use an official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .

# Install build dependencies
RUN pip install build

# Copy the src directory
COPY src ./src

# Install dependencies directly from pyproject.toml via pip
RUN pip install --no-cache-dir .

# Copy the entrypoint script
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Copy the alembic.ini file
COPY alembic.ini ./

# Set the entrypoint
ENTRYPOINT ["./entrypoint.sh"]

# Command to run the FastAPI application using uvicorn
CMD ["uvicorn", "hrms_back.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]