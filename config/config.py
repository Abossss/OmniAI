import os

# 配置文件
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 知识库文件路径（使用绝对路径）
KNOWLEDGE_FILE = os.path.join(DATA_DIR, 'knowledge.json')

# Ollama 模型名称
OLLAMA_MODEL = "qwen2"

# 日志配置
LOG_FILE = os.path.join(BASE_DIR, 'agent.log')
LOG_LEVEL = "DEBUG"
