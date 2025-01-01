from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_socketio import SocketIO
import paramiko
from functools import wraps
import json
import os
import subprocess
import threading
import time
import hashlib
import secrets
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.update(
    SECRET_KEY=secrets.token_hex(32),
    PERMANENT_SESSION_LIFETIME=timedelta(hours=1),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,  # 开发环境设为False，生产环境设为True
    SESSION_COOKIE_SAMESITE='Lax'
)
socketio = SocketIO(app, async_mode='threading')

# 保存主机配置的文件
HOSTS_FILE = 'hosts.json'

def save_hosts(hosts):
    try:
        with open(HOSTS_FILE, 'w') as f:
            json.dump(hosts, f, indent=4)
    except Exception as e:
        print(f"Error saving hosts: {str(e)}")
        return False
    return True

def load_hosts():
    try:
        if os.path.exists(HOSTS_FILE):
            with open(HOSTS_FILE, 'r') as f:
                return json.load(f)
    except Exception as e:
        print(f"Error loading hosts: {str(e)}")
    return {}

# 添加密码加密函数
def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(8)
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return salt + ":" + hash_obj.hex()

def verify_password(stored_password, provided_password):
    salt, hash_value = stored_password.split(":")
    return stored_password == hash_password(provided_password, salt)

# 添加会话过期时间检查
def check_session_expired():
    if 'login_time' not in session:
        return True
    try:
        login_time = datetime.fromisoformat(session['login_time'])
        if datetime.now() - login_time > timedelta(hours=1):
            session.clear()
            return True
    except Exception:
        return True
    return False

# 增强的登录验证装饰器
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            flash('请先登录', 'error')
            return redirect(url_for('login'))
        
        if check_session_expired():
            flash('会话已过期，请重新登录', 'error')
            return redirect(url_for('login'))
            
        # 只对POST请求检查CSRF token
        if request.method == 'POST':
            form_token = request.form.get('csrf_token')
            session_token = session.get('csrf_token')
            if not form_token or not session_token or form_token != session_token:
                flash('无效的请求，请重试', 'error')
                return redirect(url_for('hosts'))
                
        return f(*args, **kwargs)
    return decorated_function

# 添加CSRF token生成函数
def generate_csrf_token():
    if 'csrf_token' not in session:
        session['csrf_token'] = secrets.token_hex(32)
    return session['csrf_token']

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 如果已经登录，直接跳转到主机列表
    if 'logged_in' in session and not check_session_expired():
        return redirect(url_for('hosts'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(f"Login attempt - Username: {username}")  # 调试信息
        
        if username == 'admin' and password == 'password':
            print("Login successful")  # 调试信息
            session['logged_in'] = True
            session['username'] = username
            session['login_time'] = datetime.now().isoformat()
            session['csrf_token'] = secrets.token_hex(32)
            print(f"Session data: {dict(session)}")  # 调试信息
            flash('登录成功', 'success')
            return redirect(url_for('hosts'))
        else:
            print("Login failed")  # 调试信息
            flash('用户名或密码错误', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('已退出登录', 'info')
    return redirect(url_for('login'))

@app.route('/hosts')
@login_required
def hosts():
    hosts = load_hosts()
    return render_template('hosts.html', 
                         username=session.get('username'), 
                         hosts=hosts,
                         csrf_token=session.get('csrf_token'))

@app.route('/host/add', methods=['POST'])
@login_required
def add_host():
    try:
        # 检查CSRF token
        if not session.get('csrf_token'):
            session['csrf_token'] = secrets.token_hex(32)
        
        form_token = request.form.get('csrf_token')
        if not form_token or form_token != session.get('csrf_token'):
            flash('无效的请求，请重试', 'error')
            return redirect(url_for('hosts'))
            
        name = request.form.get('name')
        hostname = request.form.get('hostname')
        port = request.form.get('port', '22')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not all([name, hostname, username, password]):
            flash('请填写所有必要信息', 'error')
            return redirect(url_for('hosts'))
        
        hosts = load_hosts()
        hosts[name] = {
            'hostname': hostname,
            'port': port,
            'username': username,
            'password': password
        }
        save_hosts(hosts)
        flash('主机添加成功', 'success')
        return redirect(url_for('hosts'))
        
    except Exception as e:
        print(f"Add host error: {str(e)}")
        flash('添加主机时发生错误', 'error')
        return redirect(url_for('hosts'))

@app.route('/host/delete/<name>')
@login_required
def delete_host(name):
    hosts = load_hosts()
    if name in hosts:
        del hosts[name]
        save_hosts(hosts)
        flash('主机删除成功', 'success')
    return redirect(url_for('hosts'))

@app.route('/terminal')
@login_required
def terminal():
    host_name = request.args.get('host_name')
    if not host_name:
        return redirect(url_for('hosts'))
    
    hosts = load_hosts()
    host = hosts.get(host_name)
    if not host:
        flash('主机不存在', 'error')
        return redirect(url_for('hosts'))
        
    return render_template('terminal.html', 
                         username=session.get('username'),
                         host=host,
                         host_name=host_name,
                         csrf_token=session.get('csrf_token'))

@socketio.on('connect')
def connect():
    if 'logged_in' not in session:
        return False
    socketio.emit('debug_info', {'message': '已连接到服务器'})
    return True

@socketio.on('connect_host')
def connect_host(data):
    host_name = data.get('host_name')
    hosts = load_hosts()
    host = hosts.get(host_name)
    
    if not host:
        return {'error': '主机不存在'}
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=host['hostname'],
            port=int(host['port']),
            username=host['username'],
            password=host['password']
        )
        session['ssh'] = ssh
        channel = ssh.invoke_shell()
        session['channel'] = channel
        return {'success': True}
    except Exception as e:
        return {'error': str(e)}

@socketio.on('data')
def handle_data(data):
    if 'channel' in session:
        channel = session['channel']
        channel.send(data)

@socketio.on('disconnect_ssh')
def disconnect_ssh():
    try:
        if 'channel' in session:
            session['channel'].close()
        if 'ssh' in session:
            session['ssh'].close()
        session.pop('channel', None)
        session.pop('ssh', None)
        socketio.emit('debug_info', {'message': '已断开SSH连接'})
    except Exception as e:
        socketio.emit('debug_info', {'message': f'断开连接时发生错误: {str(e)}'})

@socketio.on('disconnect')
def disconnect():
    try:
        disconnect_ssh()
    except Exception as e:
        print(f"Disconnect error: {str(e)}")

def run_command(command):
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            universal_newlines=True
        )
        output, error = process.communicate()
        return output + error
    except Exception as e:
        return str(e)

@app.route('/test_connection', methods=['POST'])
def test_connection():
    host = request.form.get('hostname')
    port = request.form.get('port', '22')
    
    results = {
        'ping': run_command(f'ping -c 3 {host}'),
        'traceroute': run_command(f'traceroute {host}'),
        'telnet': run_command(f'timeout 5 telnet {host} {port} 2>&1 || echo "Connection timed out"'),
        'port_check': run_command(f'nc -zv {host} {port} 2>&1')
    }
    return jsonify(results)

@socketio.on('connect_ssh')
def connect_ssh(data):
    try:
        hostname = data.get('hostname')
        port = int(data.get('port', 22))
        username = data.get('username')
        password = data.get('password')

        # 发送调试信息
        socketio.emit('debug_info', {'message': f'开始连接到 {hostname}:{port}'})

        # 创建SSH客户端
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # 设置超时
        socketio.emit('debug_info', {'message': '设置连接超时为30秒'})
        
        # 尝试连接
        ssh.connect(
            hostname=hostname,
            port=port,
            username=username,
            password=password,
            timeout=30,
            allow_agent=False,
            look_for_keys=False
        )
        
        socketio.emit('debug_info', {'message': 'SSH连接成功'})
        
        # 创建通道
        channel = ssh.invoke_shell(
            term='xterm',
            width=80,
            height=24
        )
        channel.settimeout(30)
        
        socketio.emit('debug_info', {'message': 'Shell通道已创建'})
        
        # 保存到session
        session['ssh'] = ssh
        session['channel'] = channel
        
        # 启动后台任务读取输出
        def read_output():
            while True:
                try:
                    if channel.recv_ready():
                        output = channel.recv(1024).decode('utf-8', 'ignore')
                        socketio.emit('output', {'output': output})
                    socketio.sleep(0.01)
                except Exception as e:
                    socketio.emit('debug_info', {'message': f'读取输出错误: {str(e)}'})
                    break
        
        socketio.start_background_task(read_output)
        socketio.emit('ssh_connected')
        
    except Exception as e:
        error_msg = f'连接错误: {str(e)}'
        socketio.emit('debug_info', {'message': error_msg})
        socketio.emit('ssh_error', {'error': error_msg})

@app.errorhandler(Exception)
def handle_error(error):
    print(f"Error: {str(error)}")
    flash('发生错误，请重试', 'error')
    return redirect(url_for('hosts'))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000) 