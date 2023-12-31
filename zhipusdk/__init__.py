import os

from .model_api import model_api

api_key = os.environ.get("ZHIPU_API_KEY")

api_timeout_seconds = 300

model_api_url = os.environ.get(
    "zhipusdk_MODEL_API_URL", "https://open.bigmodel.cn/api/paas/v3/model-api"
)
