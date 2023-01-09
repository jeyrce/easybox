#!/usr/bin/env bash
# coding: utf-8
set -o errexit
# 定时清理文件夹避免挂载点爆满，不进行递归

target_dir=${1:?}          # 需要管理的文件夹，必填
threshold=${2:-10485760}   # 空闲空间，默认不少于 10GiB
# 黑名单，优先删除
black_list="*.tmp|*.swap|*.swp|*.log"
# 白名单，永不删除(同一个目标被定义时优先级 白 > 黑)
white_list="latest|offline_repo|udcp-auto.sh|404.jpg"
# todo: 从命令行参数读取黑白名单

if [ ! -d "$target_dir" ]; then
    echo "文件夹不存在 $target_dir"
    exit 1
fi

# 优先清理在黑名单中但是不在白名单的文件
black_items=$(ls -t /udcp/udcp |grep -E "$black_list" |grep -vE "$white_list")
for item in ${black_items[*]}; do
    item="$target_dir/$item"
    if [ "$item" == "/" ]; then
        break
    fi
    rm -rf "${item:-/tmp/xyz}"
done

# 逐个删除旧文件，直到满足阈值
while true; do
    free_size=$(df --output=avail "$target_dir" |tail -n 1)
    if [ $free_size -ge $threshold ]; then
        echo "符合域值退出"
        break
    fi
    oldest=$(ls -t "$target_dir" |grep -vE "$white_list" | tail -n 1)
    oldest="$target_dir/$oldest"
    if [ "$oldest" == "/" ]; then
        break
    fi
    echo "即将删除 $oldest"
    rm -rf "${oldest:-/tmp/xyz}"
done

exit 0
