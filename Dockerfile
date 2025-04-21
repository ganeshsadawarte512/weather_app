# 1. Use the official Python base image
FROM python:3.10-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory in container
WORKDIR /app

# 4. Copy dependency list to container
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# 6. Copy entire Django project into container
COPY . .

# 7. Expose the port your app runs on
EXPOSE 8000

# 8. Default command to run the Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
