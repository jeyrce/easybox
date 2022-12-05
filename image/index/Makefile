version:=latest

.phony: all
all: image

.phony: image
image:
	echo "构建docker镜像并上传"
	docker buildx build \
		--platform linux/amd64,linux/arm/v8,linux/386 \
		--build-arg version=${version} \
		-t jeyrce/index:${version} \
		--pull \
		--push \
		.
