pypi:=https://mirrors.aliyun.com/pypi/simple/

.phony: all
all: image

.phony: image
image:
	echo "构建docker镜像并上传"
	docker buildx build \
		--platform=linux/amd64,linux/arm64/v8 \
		--build-arg pypi=${pypi} \
		-t jeyrce/ansible:latest \
		--pull \
		--push \
		.
