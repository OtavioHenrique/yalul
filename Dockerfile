FROM python:3.8.3-alpine3.11

WORKDIR /app
ADD . /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip install -r requirements.txt

CMD ["bin/yalul"]