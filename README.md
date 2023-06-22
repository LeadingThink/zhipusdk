# 〇、缘起

此仓库之缘起，可以追溯到 `清华` 与 `智谱` 对**公益项目**——[`在问`](https://www.zaiwen.top) 的支持。他们为 `在问` 提供了一定额度的 API 使用量，使得 `在问` 能够向公众提供基于 `ChatGLM-130B` 的问答服务。

在问团队使用 `ChatGLM-130B` 的过程中，遇到了不少问题。我们尝试将问题报告给官方，我们也尝试去尽我们所能。

下面，是我们的努力。

# 一、说明

**就其要点**

## 1. 官方 `zhipuai` 在输出英文时会少空格

修改 `sse_client.py`， 将其中删除空格的代码移除。

此外， `sse_client.py` 的最后一个函数少一个返回值，现已补上。

## 2. 130b 在流式返回中，代码与文字之间缺少空格

在 `zhipusdk/utils` 中新建了一个 `counter.py` 实现一个计数器；

在 `sse_client.py` 的基础上新建一个 `sse_client_for_130.py` ，并在其中添加代码，根据模型返回的
` ``` `(三反引号)，来添加换行，在`奇数`的`前面`添加两个换行，在`偶数`的`后面`添加两个换行。

修改 `zhipusdk/model_api/api.py`，让 6b 的模型走原先的 `sse_client.py`； 让 130b 的模型走新的 `sse_client_for_130b.py`；以实现两不干扰。( 6b 模型的输出中不会缺少换行。)

## 3. 其他

- 官方的 `zhipuai` 下载自 [PyPI](https://pypi.org/project/zhipuai/#files)。下载日期是: **2023-6-13**。
- `example` 文件夹是官方原始的例子，除了把其中的 `zhipuai` 替换为 `zhipusdk` 外，没有任何更改；也未进行测试。理论上， `zhipusdk` 和官方的包使用方法一模一样。

# 二、License

`zhipuai` 采用的是 `MIT` 许可证，详见 [PyPI](https://pypi.org/project/zhipuai/#files)。但在软件包中未发现版权声明文件，故作此说明。本仓库未包含原始的 `MIT` 许可文件，完全是这个原因。
