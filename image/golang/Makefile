hub:=jeyrce/golang
version:=1.19.1-alpine

.PHONY: all
all:
	@-docker buildx rm tmp
	docker buildx create --name tmp --bootstrap --use
	docker buildx build -t ${hub}:${version} \
		--build-arg version=${version} \
		--platform linux/386,linux/amd64,linux/arm64 \
		--push \
		.
	@-docker buildx rm tmp
