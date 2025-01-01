FROM python:3.9-slim

# 安装必要的系统包
RUN apt-get update && apt-get install -y \
    openssh-server \
    iputils-ping \
    traceroute \
    && rm -rf /var/lib/apt/lists/*

# 配置SSH服务
RUN mkdir /var/run/sshd
RUN echo 'root:default_password' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 设置启动脚本权限
COPY start.sh /start.sh
RUN chmod +x /start.sh

# 暴露端口
EXPOSE 8000

# 启动服务
CMD ["/start.sh"] 