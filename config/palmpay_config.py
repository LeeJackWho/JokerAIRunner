# PP登录账号（真实值走环境变量，禁止提交）
import os

PP_MOBILE_NO = os.getenv("PP_MOBILE_NO", "<YOUR_MOBILE>")
PP_PIN = os.getenv("PP_PIN", "<YOUR_PIN>")
