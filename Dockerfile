# syntax=docker/dockerfile:1

FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install pipenv and dependencies
COPY Pipfile Pipfile.lock /app/
RUN pip install --no-cache-dir pipenv && pipenv install --deploy --ignore-pipfile

# Copy the Django app code
COPY ./healthcarebackend /app

# Run migrations and start the server
CMD ["pipenv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
