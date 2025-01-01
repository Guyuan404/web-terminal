PS C:\Users\guyuan\Desktop\fsdownload\dockerv10> docker-compose build
time="2025-01-01T09:35:11+08:00" level=warning msg="C:\\Users\\guyuan\\Desktop\\fsdownload\\dockerv10\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Building 4.9s (18/18) FINISHED                                                                 docker:desktop-linux
 => [web internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 935B                                                                               0.0s
 => [web internal] load metadata for docker.io/library/python:3.9-slim                                             2.4s
 => [web auth] library/python:pull token for registry-1.docker.io                                                  0.0s
 => [web internal] load .dockerignore                                                                              0.0s
 => => transferring context: 71B                                                                                   0.0s
 => [web  1/11] FROM docker.io/library/python:3.9-slim@sha256:caaf1af9e23adc6149e5d20662b267ead9505868ff07c7673dc  0.1s
 => => resolve docker.io/library/python:3.9-slim@sha256:caaf1af9e23adc6149e5d20662b267ead9505868ff07c7673dc4a7166  0.1s
 => [web internal] load build context                                                                              0.0s
 => => transferring context: 35.70kB                                                                               0.0s
 => CACHED [web  2/11] WORKDIR /app                                                                                0.0s
 => CACHED [web  3/11] RUN apt-get update && apt-get install -y     openssh-server     iputils-ping     tracerout  0.0s
 => CACHED [web  4/11] RUN echo 'root:default_password' | chpasswd                                                 0.0s
 => CACHED [web  5/11] RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_confi  0.0s
 => CACHED [web  6/11] COPY requirements.txt .                                                                     0.0s
 => CACHED [web  7/11] RUN pip install --no-cache-dir -r requirements.txt                                          0.0s
 => [web  8/11] COPY templates/ templates/                                                                         0.1s
 => [web  9/11] COPY main.py .                                                                                     0.2s
 => [web 10/11] COPY start.sh /start.sh                                                                            0.2s
 => [web 11/11] RUN chmod +x /start.sh                                                                             0.5s
 => [web] exporting to image                                                                                       1.0s
 => => exporting layers                                                                                            0.6s
 => => exporting manifest sha256:fbd6211f8f043e712a6c8e44f6bad92c380cb11f74216f51aa8572e4024e2770                  0.0s
 => => exporting config sha256:d8bd1a6a2902702c14b6fdb9cf16f5c2b23fd171ee43305e13df7d4a548bce79                    0.0s
 => => exporting attestation manifest sha256:49601a7310c156ef6fc04a8f837c5b11ac25bf57be741c3ed01deb714db0d25e      0.1s
 => => exporting manifest list sha256:fc2b843f02fedfc4e8c4e2f684e6cac4640448e9205b9e75ba065f7bdbfaef2b             0.0s
 => => naming to docker.io/library/dockerv10-web:latest                                                            0.0s
 => => unpacking to docker.io/library/dockerv10-web:latest                                                         0.2s
 => [web] resolving provenance for metadata file                                                                   0.0s
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10> docker-compose up -d
time="2025-01-01T09:35:26+08:00" level=warning msg="C:\\Users\\guyuan\\Desktop\\fsdownload\\dockerv10\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 2/2
 ✔ Network dockerv10_web_network  Created                                                                          0.1s
 ✔ Container dockerv10-web-1      Started                                                                          0.7s
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10> docker ps -a
CONTAINER ID   IMAGE           COMMAND       CREATED          STATUS          PORTS                            NAMES
214ae99facf4   dockerv10-web   "/start.sh"   52 seconds ago   Up 51 seconds   22/tcp, 0.0.0.0:8000->8000/tcp   dockerv10-web-1
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10> docker stop 214ae99facf4
214ae99facf4
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10>
PS C:\Users\guyuan\Desktop\fsdownload\dockerv10> docker-compose up
time="2025-01-01T09:36:46+08:00" level=warning msg="C:\\Users\\guyuan\\Desktop\\fsdownload\\dockerv10\\docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion"
[+] Running 1/0
 ✔ Container dockerv10-web-1  Created                                                                              0.0s
Attaching to web-1
web-1  | Starting OpenBSD Secure Shell server: sshd.
web-1  | /usr/local/lib/python3.9/site-packages/paramiko/pkey.py:100: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
web-1  |   "cipher": algorithms.TripleDES,
web-1  | /usr/local/lib/python3.9/site-packages/paramiko/transport.py:258: CryptographyDeprecationWarning: TripleDES has been moved to cryptography.hazmat.decrepit.ciphers.algorithms.TripleDES and will be removed from cryptography.hazmat.primitives.ciphers.algorithms in 48.0.0.
web-1  |   "class": algorithms.TripleDES,
web-1  | WebSocket transport not available. Install simple-websocket for improved performance.
web-1  |  * Serving Flask app 'main' (lazy loading)
web-1  |  * Environment: production
web-1  |    WARNING: This is a development server. Do not use it in a production deployment.
web-1  |    Use a production WSGI server instead.
web-1  |  * Debug mode: off
web-1  |  * Running on all addresses.
web-1  |    WARNING: This is a development server. Do not use it in a production deployment.
web-1  |  * Running on http://172.19.0.2:8000/ (Press CTRL+C to quit)
web-1  | The WebSocket transport is not available, you must install a WebSocket server that is compatible with your async mode to enable it. See the documentation for details. (further occurrences of this error will be logged with level INFO)
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:48] "GET /socket.io/?EIO=4&transport=polling&t=PGVWXua HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:48] "POST /socket.io/?EIO=4&transport=polling&t=PGVWXuw&sid=H40E5iIoBHriEBC_AAAA HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:48] "GET /socket.io/?EIO=4&transport=polling&t=PGVWXux&sid=H40E5iIoBHriEBC_AAAA HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:53] "POST /socket.io/?EIO=4&transport=polling&t=PGVWZ80&sid=H40E5iIoBHriEBC_AAAA HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:53] "GET /socket.io/?EIO=4&transport=polling&t=PGVWXvG&sid=H40E5iIoBHriEBC_AAAA HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:53] "GET /terminal?host_name=claw HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:53] "GET /login HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:54] "GET /favicon.ico HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:54] "GET /hosts HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:36:54] "GET /login HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:06] "POST /login HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:06] "GET /hosts HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:06] "GET /favicon.ico HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:06] "GET /hosts HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "GET /terminal?host_name=claw HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "GET /socket.io/?EIO=4&transport=polling&t=PGVWfBA HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "POST /socket.io/?EIO=4&transport=polling&t=PGVWfBf&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "GET /socket.io/?EIO=4&transport=polling&t=PGVWfBf.0&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "GET /favicon.ico HTTP/1.1" 302 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:18] "GET /hosts HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:19] "GET /socket.io/?EIO=4&transport=polling&t=PGVWfD2&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:19] "POST /socket.io/?EIO=4&transport=polling&t=PGVWfVt&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | Exception (client): Error reading SSH protocol banner
web-1  | Traceback (most recent call last):
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2292, in _check_banner
web-1  |     buf = self.packetizer.readline(timeout)
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/packet.py", line 374, in readline
web-1  |     buf += self._read_timeout(timeout)
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/packet.py", line 603, in _read_timeout
web-1  |     raise EOFError()
web-1  | EOFError
web-1  |
web-1  | During handling of the above exception, another exception occurred:
web-1  |
web-1  | Traceback (most recent call last):
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2113, in run
web-1  |     self._check_banner()
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2296, in _check_banner
web-1  |     raise SSHException(
web-1  | paramiko.ssh_exception.SSHException: Error reading SSH protocol banner
web-1  |
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:21] "GET /socket.io/?EIO=4&transport=polling&t=PGVWfW4&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:25] "GET /socket.io/?EIO=4&transport=polling&t=PGVWfoW&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:25] "POST /socket.io/?EIO=4&transport=polling&t=PGVWgoq&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
web-1  | Exception (client): Error reading SSH protocol banner
web-1  | Traceback (most recent call last):
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2292, in _check_banner
web-1  |     buf = self.packetizer.readline(timeout)
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/packet.py", line 374, in readline
web-1  |     buf += self._read_timeout(timeout)
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/packet.py", line 603, in _read_timeout
web-1  |     raise EOFError()
web-1  | EOFError
web-1  |
web-1  | During handling of the above exception, another exception occurred:
web-1  |
web-1  | Traceback (most recent call last):
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2113, in run
web-1  |     self._check_banner()
web-1  |   File "/usr/local/lib/python3.9/site-packages/paramiko/transport.py", line 2296, in _check_banner
web-1  |     raise SSHException(
web-1  | paramiko.ssh_exception.SSHException: Error reading SSH protocol banner
web-1  |
web-1  | 172.19.0.1 - - [01/Jan/2025 01:37:26] "GET /socket.io/?EIO=4&transport=polling&t=PGVWgp9&sid=aUJ_xNU1vvONEe5cAAAC HTTP/1.1" 200 -
