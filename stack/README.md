### compose

```shell
export DATA_DIR=/data
docker compose up -d -f xxx.yml ...
```

### stack

```shell
export DATA_DIR=/data
docker stack deploy dev --prune -c xxx.yml
```
