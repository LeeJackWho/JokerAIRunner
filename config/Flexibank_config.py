# Flexibank 测试环境配置
# 设备/账号信息走环境变量，禁止提交真实值。
import os

FB_DEVICE_ID = os.getenv("FB_DEVICE_ID", "<YOUR_DEVICE_ID>")
FB_DEVICE_TYPE = "ANDROID"
FB_CLIENT_VER = "3.12.4&604021107"

# FB端登录手机号
FB_PHONE = os.getenv("FB_PHONE", "<YOUR_PHONE>")
# FB端登录密码
FB_PASSWORD = os.getenv("FB_PASSWORD", "<YOUR_PASSWORD>")
