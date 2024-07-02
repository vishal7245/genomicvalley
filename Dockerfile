# This Dockerfile is used to deploy a simple single-container Reflex app instance.
FROM python:3.11

# Set environment variable for virtual environment
ENV VIRTUAL_ENV=/opt/venv

# Install venv and create a virtual environment
RUN python -m venv $VIRTUAL_ENV

# Ensure the virtual environment is in the PATH
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .

# Install app requirements in the container
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD reflex db migrate && reflex run --env prod
