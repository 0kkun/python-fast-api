FROM python:3.9-slim

RUN apt update \
    && apt install -y default-mysql-client \
    && apt-get -y install gcc libmariadb-dev \
    && apt install --no-install-recommends -y tzdata \
    && apt clean

WORKDIR /app

COPY requirements.txt .
# COPY ./.docker/requirements.txt .
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN pip install -U pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]