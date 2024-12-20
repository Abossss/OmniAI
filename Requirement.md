# 需求规格

## 1. 软件功能需求

该智能助手程序主要包括以下功能：

1. **用户交互**：用户可以通过输入问题与助手进行对话，助手返回基于本地知识库、加载的文档或网络搜索的回答。
2. **知识库查询**：程序支持本地知识库查询，用户提出的任何问题会首先从知识库中查找相关答案。
3. **文档查询**：用户提出的问题如果知识库中没有相关答案，助手会从预先加载的文档（如 `.docx` 和 `.pdf` 文件）中检索相关内容。
4. **联网查询**：如果文档中也没有答案，助手将通过外部网络查询获取答案（使用 `Ollama` 模型框架）。
5. **记忆功能**：程序具有短期和长期记忆管理，能够记住用户的输入和常见问题，以便提供更精准的回答。
6. **问题与回答存储**：每次用户提问时，问题与回答会存储在 `knowledge.json` 文件中，文件会保存在 `data/` 目录下。

## 2. 环境需求

- **操作系统**：支持 Windows、macOS、Linux。
- **Python版本**：3.6 及以上。

## 3. 所需库

1. `ollama~=0.4.0`：与 Ollama 模型进行交互的 Python 库，用于联网查询。
2. `docx~=0.2.4`：用于读取 `.docx` 文件。
3. `python-docx~=1.1.2`：另一个用于处理 `.docx` 文件的库，兼容性较好。
4. `pdfplumber~=0.11`：用于读取 `.pdf` 文件。
5. `json`：用于解析和存储 JSON 格式的数据（Python 标准库，无需单独安装）。
6. `logging`：用于日志记录和调试（Python 标准库，无需单独安装）。
7. `unittest`：用于单元测试（Python 标准库，无需单独安装）。



## 4. 配置文件

### `config.py`

- **`KNOWLEDGE_FILE`**：知识库文件路径，默认为 `data/knowledge.json`。
- **`OLLAMA_MODEL`**：使用的 Ollama 模型框架，默认为 `qwen2`。
- **`LOG_FILE`**：日志文件路径，默认为 `agent.log`。
- **`LOG_LEVEL`**：日志级别，默认为 `DEBUG`。

## 5. 其他需求

### 5.1 数据存储位置

- 所有问题与回答会被存储在 `data/knowledge.json` 文件中，文件内容采用 JSON 格式保存，键为问题，值为对应的回答。

### 5.2 打包为可执行文件

程序支持通过 `PyInstaller` 打包为独立的可执行文件，以便于分发和部署。打包命令如下：

```bash
pyinstaller --onefile --windowed scripts/run_agent.py
