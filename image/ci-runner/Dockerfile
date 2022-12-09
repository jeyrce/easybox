FROM docker:dind AS runner
ARG commit
LABEL desc="runner for gitlab-ci" \
      poweredBy="https://github.com/jeyrce/easybox" \
      commit="${commit}"
RUN apk add --no-cache \
    bash git make curl sqlite gcc && \
    make --version && \
    git --version && \
    curl --version && \
    ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo "Asia/Shanghai" > /etc/timezone

