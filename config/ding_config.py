# 钉钉配置信息
# 敏感凭据一律从环境变量读取，禁止在代码仓库中提交真实 access_token / 加签密钥。
# 本地使用方式（示例）：
#   export DING_WEBHOOK_URL="https://oapi.dingtalk.com/robot/send?access_token=<你的token>"
#   export DING_SECRET="<你的加签密钥>"
import os

# pp测试群（占位，真实值走环境变量）
DING_WEBHOOK_URL = os.getenv("DING_WEBHOOK_URL", "https://oapi.dingtalk.com/robot/send?access_token=<YOUR_ACCESS_TOKEN>")
DING_SECRET = os.getenv("DING_SECRET", "<YOUR_SIGN_SECRET>")
