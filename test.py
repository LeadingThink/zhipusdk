import asyncio
import zhipusdk


async def async_request_glm(prompt: str):
    print(prompt)
    response = zhipusdk.model_api.sse_invoke(
        model="chatglm_130b",
        prompt=prompt,
        temperature=0.95,
        top_p=0.7,
        incremental=False,
    )
    for event in response.events():
        print(event.data, end="")


prompt = """
请用 Java 写一个 hello world， 我已经配置了环境
"""

asyncio.run(async_request_glm(prompt))
