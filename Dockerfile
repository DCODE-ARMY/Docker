FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80","--log-level", "debug", "DjangoWebProject1.wsgi:application"]