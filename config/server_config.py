# 服务器配置信息
# 内网地址与凭据走环境变量，禁止提交真实值。
import os

REMOTE_SERVER_URL = os.getenv("REMOTE_SERVER_URL", "<YOUR_SERVER_IP>")
USER_NAME = os.getenv("REMOTE_USER", "root")
PASSWORD = os.getenv("REMOTE_PASSWORD", "<YOUR_PASSWORD>")
REMOTE_PATH = os.getenv("REMOTE_PATH", "/root/wl/report")
PRIVATE_KEY_PATH = os.getenv("PRIVATE_KEY_PATH", r"C:\Users\Administrator\.ssh\id_rsa")
