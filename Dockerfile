FROM python:3.12.1-alpine3.18

WORKDIR /shop

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]