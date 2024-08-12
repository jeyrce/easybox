FROM python:3.11.9-slim
WORKDIR /app
COPY lottery.py .
RUN pip install -U pip && \
    pip install requests

ENV LOTTERY_START_AT=2024-08-12 \
    LOTTERY_TIMES=15 \
    ROBOT_TOKEN='****'

CMD ["sh","-c","python", "/app/lottery.py"]
