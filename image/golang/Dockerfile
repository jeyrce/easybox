ARG version=1.19.1-alpine
FROM golang:${version} as builder
ENV GOPATH=/go
ENV GOOS=linux
ENV CGO_ENABLED=0
WORKDIR /go/src/
COPY . .
RUN apk add make git
