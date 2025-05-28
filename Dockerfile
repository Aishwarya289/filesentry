# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (can be overridden in Jenkins)
CMD ["python", "main.py", "sample_dir"]
