#!/bin/bash

# 启动SSH服务
service ssh start

# 检查SSH服务状态
service ssh status

# 使用gunicorn启动Flask应用
exec gunicorn --bind 0.0.0.0:8000 --worker-class eventlet -w 1 main:app 