FROM python:3.9-alpine

# setup directory for application
WORKDIR /app

# to keep docker cache on this layer we only copy requirements.txt
# then install dependecies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apk add --no-cache mysql-client

# copy source code
ADD . /app
