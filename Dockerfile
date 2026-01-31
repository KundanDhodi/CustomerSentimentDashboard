# Step 1: Use Python base image
FROM python:3.10-slim

# Step 2: Create a working directory inside container
WORKDIR /app

# Step 3: Copy dependency list into container
COPY requirements.txt .

# Step 4: Install dependencies (for future backend)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy project files (code will be added later)
COPY . .

# Step 6: Expose backend port
EXPOSE 8000

# Step 7: Temporary command (no backend yet)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

