FROM alpine:latest

WORKDIR /data

LABEL author="Jeyrce Lu<jeyrce@gmail.com>" \
      poweredBy="https://github.com/jeyrce/easybox"

ADD rsyncd.conf /etc

USER root:root

RUN apk add rsync && mkdir -p "/data"

VOLUME ["/data"]

EXPOSE 873

CMD ["rsync", "--daemon", "--no-detach"]
