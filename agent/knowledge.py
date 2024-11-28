import json
import os

class KnowledgeBase:
    def __init__(self, knowledge_file):
        self.knowledge_file = knowledge_file

        # 检查文件是否存在并加载数据
        if os.path.exists(knowledge_file):
            with open(knowledge_file, 'r', encoding='utf-8') as file:
                try:
                    # 尝试读取并解析 JSON 文件
                    self.knowledge = json.load(file)
                except json.JSONDecodeError:
                    self.knowledge = {}
        else:
            self.knowledge = {}

    def query(self, keyword):
        """查询本地知识库"""
        return self.knowledge.get(keyword, "抱歉，我还没有相关知识。")
