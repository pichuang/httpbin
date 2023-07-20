FROM docker.io/library/ubuntu:18.04

LABEL org.opencontainers.image.title = "httpbin" \
      org.opencontainers.image.description "A simple HTTP service." \
      org.opencontainers.image.authors = "Kenneth Reitz, Phil Huang <phil.huang@microsoft.com>" \
      org.opencontainers.image.source = "https://github.com/pichuang/httpbin" \
      org.opencontainers.image.licenses = "ISC License" \
      org.opencontainers.image.url = "https://httpbin.org" \
      org.opencontainers.image.version = "20230721" \
      org.opencontainers.image.base.name = "library/ubuntu:22.04" \

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update -y && apt install python3-pip git -y && pip3 install --no-cache-dir pipenv

ADD Pipfile Pipfile.lock /httpbin/
WORKDIR /httpbin
RUN /bin/bash -c "pip3 install --no-cache-dir -r <(pipenv lock -r)"

ADD . /httpbin
RUN pip3 install --no-cache-dir /httpbin

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "httpbin:app", "-k", "gevent"]
