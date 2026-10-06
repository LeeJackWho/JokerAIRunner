# B端测试环境配置（真实值走环境变量，禁止提交）
import os

B_DEVICE_ID = os.getenv("B_DEVICE_ID", "<YOUR_DEVICE_ID>")
B_DEVICE_TYPE = "ANDROID"
B_CLIENT_VER = "3.12.4&604021107"

# B端登录手机号
B_PHONE = os.getenv("B_PHONE", "<YOUR_PHONE>")
# B端登录密码
B_PASSWORD = os.getenv("B_PASSWORD", "<YOUR_PASSWORD>")
