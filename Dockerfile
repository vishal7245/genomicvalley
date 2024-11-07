FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Copy local context to `/app` inside container
WORKDIR /app
COPY . .

# Install app requirements and reflex in the container
RUN pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Download all npm dependencies and compile frontend
RUN reflex export --frontend-only --no-zip

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL