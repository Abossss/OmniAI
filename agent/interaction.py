import os
import docx
import pdfplumber
import json
from agent.memory import Memory
from agent.web_search import WebSearch


class Interaction:
    def __init__(self, knowledge_file=None):
        self.memory = Memory()

        # 设置正确的 knowledge.json 文件路径
        self.base_dir = os.path.dirname(os.path.dirname(__file__))  # 获取 Agent\agent 目录路径
        self.knowledge_file = os.path.join(self.base_dir, 'data', 'knowledge.json') if not knowledge_file else knowledge_file

        # 加载文档内容
        self.documents = self.load_documents(os.path.join(self.base_dir, 'docs'))
        self.load_knowledge()

    def load_knowledge(self):
        """加载现有的知识库（如果存在）"""
        if os.path.exists(self.knowledge_file):
            with open(self.knowledge_file, 'r', encoding='utf-8') as f:
                try:
                    self.knowledge = json.load(f)
                except json.JSONDecodeError:
                    self.knowledge = {}
        else:
            self.knowledge = {}

    def save_knowledge(self):
        """保存新的问题和答案到 knowledge.json 文件中"""
        # 确保 data 目录存在
        os.makedirs(os.path.dirname(self.knowledge_file), exist_ok=True)

        with open(self.knowledge_file, 'w', encoding='utf-8') as f:
            json.dump(self.knowledge, f, ensure_ascii=False, indent=4)

    def load_documents(self, docs_folder):
        """从 docs 文件夹加载所有的文档内容（.docx 和 .pdf）"""
        if not os.path.exists(docs_folder):
            raise FileNotFoundError(f"找不到文件夹: {docs_folder}")

        documents = []
        for filename in os.listdir(docs_folder):
            file_path = os.path.join(docs_folder, filename)
            if filename.endswith('.docx'):
                documents.append(self.extract_docx(file_path))
            elif filename.endswith('.pdf'):
                documents.append(self.extract_pdf(file_path))
        return documents

    def extract_docx(self, file_path):
        """提取 .docx 文件内容"""
        try:
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])
            return text
        except Exception as e:
            return f"无法提取 {file_path} 中的内容: {e}"

    def extract_pdf(self, file_path):
        """提取 .pdf 文件内容"""
        try:
            with pdfplumber.open(file_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()
            return text
        except Exception as e:
            return f"无法提取 {file_path} 中的内容: {e}"

    def interact(self, user_input):
        """处理用户输入并返回答复"""
        self.memory.remember_short_term(user_input)

        # 1. 查询文档内容
        local_response = self.retrieve_from_documents(user_input)
        if local_response:
            response = local_response
        else:
            # 2. 查询联网（Ollama 模型），传递文档参数
            response = WebSearch.search(user_input, self.documents)

        # 3. 将问题和回答存入 knowledge.json
        self.store_question_answer(user_input, response)

        return response

    def store_question_answer(self, question, answer):
        """将问题和答案存入 knowledge.json 文件"""
        self.knowledge[question] = answer
        self.save_knowledge()

    def retrieve_from_documents(self, query):
        """从加载的文档内容中检索相关信息"""
        relevant_documents = []
        for document in self.documents:
            if query.lower() in document.lower():
                relevant_documents.append(document)

        if relevant_documents:
            # 将找到的文档内容拼接成一个大文本
            return "\n".join(relevant_documents)
        else:
            return None
