import asyncio
import zhipusdk


async def async_request_glm(prompt: str):
    print(prompt)
    response = zhipusdk.model_api.sse_invoke(
        model="chatglm_6b",
        prompt=prompt,
        temperature=0.95,
        top_p=0.7,
        incremental=True,
    )
    for event in response.events():
        print(event.data, end="")


asyncio.run(async_request_glm("请用Python写一个 hello world"))
