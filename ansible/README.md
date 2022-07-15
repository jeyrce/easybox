# ansible

构建自用ansible镜像，官方不知道什么原因已经几年不曾更新了。

使用方法:

```shell
docker run exec -it --rm jeyrce/ansible:latest \
    -v ./:/ansible \
    --scp-extra-args '-o StrictHostKeyChecking=no' \
    --sftp-extra-args '-o StrictHostKeyChecking=no' \
    --ssh-common-args '-o StrictHostKeyChecking=no' \
    --ssh-extra-args '-o StrictHostKeyChecking=no' \
    -i inventory/main.yaml
```
