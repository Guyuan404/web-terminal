# 🚀 Web Terminal

一个功能强大的基于Web的远程终端管理系统，支持多主机管理和SSH连接。

## ✨ 功能特点

- 🖥️ 多主机管理
- 🔐 安全的用户认证
- ⚡ 实时终端交互
- 🔒 支持HTTPS
- 📱 响应式设计
- 🌈 美观的UI界面

## 🛠️ 技术栈

- 🐍 Backend: Python Flask
- 🎨 Frontend: HTML, CSS, JavaScript
- 🔌 WebSocket: Flask-SocketIO
- 🔑 SSH: Paramiko
- 🐳 Container: Docker

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/YOUR_USERNAME/web-terminal.git
cd web-terminal
```

### 2. 使用Docker运行
```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### 3. 访问应用
浏览器访问 `http://localhost:8000`

默认登录信息：
- 👤 用户名：admin
- 🔑 密码：password

## 🔐 安全提示

在生产环境中请注意：
1. 🔒 修改默认登录密码
2. 🛡️ 启用HTTPS
3. 📦 定期更新依赖包
4. 🔍 监控系统日志

## 🌟 主要特性

### 终端管理 💻
- 实时终端交互
- 支持常见Shell命令
- 自动重连机制

### 主机管理 🏢
- 添加/删除主机
- 保存主机配置
- 快速连接

### 安全特性 🛡️
- 会话管理
- CSRF保护
- XSS防御
- 密码加密存储

## 📝 开发计划

- [ ] 支持SSH密钥认证
- [ ] 添加用户权限管理
- [ ] 实现文件传输功能
- [ ] 添加终端回放功能
- [ ] 集成系统监控

## 🤝 贡献指南

欢迎提交Pull Request或Issue！

## 📄 许可证

MIT License 