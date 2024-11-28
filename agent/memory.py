import time

class Memory:
    def __init__(self):
        self.short_term_memory = []
        self.long_term_memory = {}

    def remember_short_term(self, text):
        """将用户输入记录到短期记忆中"""
        self.short_term_memory.append((time.time(), text))
        if len(self.short_term_memory) > 5:  # 限制短期记忆大小
            self.short_term_memory.pop(0)

    def remember_long_term(self, key, value):
        """存储长期记忆"""
        self.long_term_memory[key] = value

    def retrieve_long_term(self, query):
        """检索长期记忆"""
        for key, value in self.long_term_memory.items():
            if key in query:
                return value
        return None
