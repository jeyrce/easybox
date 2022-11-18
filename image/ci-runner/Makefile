
version:=latest
commit=$(shell git symbolic-ref --short -q HEAD)

.phony: all
all:
	@echo "构建gitlab-ci基于docker的runner"
	docker buildx build -t jeyrce/ci-runner:${version} \
		--platform=linux/amd64,linux/arm64 \
		--build-arg commit=${commit} \
		--pull \
		--push \
		.
