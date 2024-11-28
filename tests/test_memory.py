import unittest
from agent.memory import Memory

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_short_term_memory(self):
        self.memory.remember_short_term("测试短期记忆")
        self.assertEqual(len(self.memory.short_term_memory), 1)

    def test_long_term_memory(self):
        self.memory.remember_long_term("关键字", "测试知识")
        self.assertEqual(self.memory.retrieve_long_term("关键字"), "测试知识")

if __name__ == '__main__':
    unittest.main()
