# -*- coding:utf-8 -*-
import posixpath

import zhipusdk
from zhipusdk.utils import jwt_token
from zhipusdk.utils.http_client import get, post, stream
from zhipusdk.utils.sse_client_for_130b import SSEClientFor130B
from zhipusdk.utils.sse_client import SSEClient
import copy


class InvokeType:
    SYNC = "invoke"
    ASYNC = "async-invoke"
    SSE = "sse-invoke"


class ModelAPI:
    @classmethod
    def invoke(cls, **kwargs):
        url = cls._build_api_url(kwargs, InvokeType.SYNC)
        return post(url, cls._generate_token(), kwargs, zhipusdk.api_timeout_seconds)

    @classmethod
    def async_invoke(cls, **kwargs):
        url = cls._build_api_url(kwargs, InvokeType.ASYNC)
        return post(url, cls._generate_token(), kwargs, zhipusdk.api_timeout_seconds)

    @classmethod
    def query_async_invoke_result(cls, task_id: str):
        url = cls._build_api_url(None, InvokeType.ASYNC, task_id)
        return get(url, cls._generate_token(), zhipusdk.api_timeout_seconds)

    @classmethod
    def sse_invoke(cls, **kwargs):
        # def sse_invode(
        #     cls,
        #     model: str,
        #     prompt: List[dict],
        #     temperature: Union[None, float] = None,
        #     top_p: Union[None, float] = None,
        #     incremental: bool = True,
        # ):
        model = kwargs["model"]
        url = cls._build_api_url(kwargs, InvokeType.SSE)
        data = stream(url, cls._generate_token(), kwargs, zhipusdk.api_timeout_seconds)

        if model == "chatglm_130b":
            try:
                incremental = kwargs["incremental"]
                if incremental:
                    return SSEClientFor130B(data)
                else:
                    # 如果全量返回，则不需要进行额外处理
                    return SSEClient(data)
            except:
                return SSEClientFor130B(data)
        else:
            return SSEClient(data)

    @staticmethod
    def _build_api_url(kwargs, *path):
        if kwargs:
            if "model" not in kwargs:
                raise Exception("model param missed")
            model = kwargs.pop("model")
        else:
            model = "-"

        return posixpath.join(zhipusdk.model_api_url, model, *path)

    @staticmethod
    def _generate_token():
        if not zhipusdk.api_key:
            raise Exception(
                "api_key not provided, you could provide it with `shell: export API_KEY=xxx` or `code: zhipusdk.api_key=xxx`"
            )

        return jwt_token.generate_token(zhipusdk.api_key)
