FROM python:3.13-slim
WORKDIR /app
RUN apt update && apt install -y build-essential libpq-dev
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000"]