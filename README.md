# easybox

构建自 `busybox:1.35.0` ，但是包含了更多常用的工具命令

## 常用工具一览

| 常用命令   | 作用     | 示例                            |
|:-------|:-------|:------------------------------|
| ping   | 排查主机网络 | ping/ping6 {ip}               |
| nc     | 排查端口   | nc -zv {ip} {port}            |
| telnet | 排查端口   | telnet {ip} {port}            |
| wget   | 下载文件   | wget "http://ip.com/x.tar.gz" |
