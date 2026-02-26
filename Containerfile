FROM python:3.11-slim

WORKDIR /app

# Install uv inside the image
RUN pip install --no-cache-dir uv

# Copy dependency definition
COPY pyproject.toml /app/

# Install deps (no lockfile yet; still fine for learning)
RUN uv sync --no-dev

# Copy app code
COPY app.py /app/

EXPOSE 8000
CMD ["uv", "run", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8000"]
