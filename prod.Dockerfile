# Stage 1: init
FROM python:3.11 as init

ARG uv=/root/.cargo/bin/uv

# Install `uv` for faster package boostrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Create virtualenv
RUN python3 -m venv /app/.venv

# Activate virtualenv and install app requirements
ENV PATH="/app/.venv/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Export static copy of frontend to /app/.web/_static
RUN reflex export --frontend-only --no-zip

# Copy static files out of /app to save space in backend image
RUN mv .web/_static /tmp/_static
RUN rm -rf .web && mkdir .web
RUN mv /tmp/_static .web/_static

# Stage 2: copy artifacts into slim image 
FROM python:3.11-slim

# Create a non-root user to run the application
RUN adduser --disabled-password --home /app reflex

# Copy application artifacts and virtualenv from init stage
WORKDIR /app
COPY --from=init --chown=reflex /app /app

# Install libpq-dev for psycopg2 (skip if not using postgres).
RUN apt-get update -y && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER reflex

# Set PATH to include virtualenv binaries
ENV PATH="/app/.venv/bin:$PATH"

# Set stopsingal and command
STOPSIGNAL SIGKILL
CMD reflex db migrate && reflex run --env prod --backend-only
