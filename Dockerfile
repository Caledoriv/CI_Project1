FROM gliderlabs/alpine:3.3

WORKDIR /myapp
COPY . /myapp

RUN apk --update add python py-pip openssl ca-certificates
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

CMD python test_task.py