ARG ARCH
ARG Platform

# FROM python:3-slim-buster-${ARCH}
FROM --platform=linux/arm64 python:3-slim-buster
# FROM --platform=linux/arm64 python:3

# COPY uname /bin/uname
# COPY uname /usr/bin/uname
# RUN chmod a+x /bin/uname
# RUN chmod a+x /usr/bin/uname
RUN pip install --no-cache-dir ansible

RUN apt-get update -y && \
   DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
   ssh-client sshpass

WORKDIR /work
