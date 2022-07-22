ARG version=3.16.0
FROM alpine:${version} AS base
LABEL author="Jeyrce Lu<jeyrce@gmail.com>" \
      poweredBy="https://github.com/jeyrce/easybox"
RUN echo "Asia/Shanghai" > /etc/timezone && \
    date
RUN mkdir -p /usr/share/zoneinfo/Asia
COPY Shanghai /etc/localtime
COPY Shanghai /usr/share/zoneinfo/Asia/Shanghai
