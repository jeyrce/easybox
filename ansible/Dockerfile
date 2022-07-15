# 从代码仓库构建较小的镜像
FROM python:3.11.0b4-slim AS builder
ARG pypi=https://mirrors.aliyun.com/pypi/simple/
ENV LANG=zh_CN.UTF-8
WORKDIR /ansible
RUN pip install --no-cache-dir -U pip -i ${pypi} && \
    pip install --no-cache-dir -U ansible -i ${pypi} && \
    rm -rf ~/.cache && \
    ansible --version
