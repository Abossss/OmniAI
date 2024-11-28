import ollama


class WebSearch:
    @staticmethod
    def search_local(query, documents):
        """从文档列表中查询答案"""
        relevant_documents = []
        for document in documents:
            if query.lower() in document.lower():
                relevant_documents.append(document)

        if relevant_documents:
            # 返回相关文档的内容
            return "\n".join(relevant_documents)
        else:
            return "抱歉，我没有找到相关的文档。"

    @staticmethod
    def search_model(query, documents):
        """使用 Ollama 模型查询答案，并考虑文档内容"""
        try:
            # 在查询模型时，可以结合文档的内容作为上下文传递
            # 这里假设你将文档内容拼接起来作为上下文（如果需要的话）
            context = "\n".join(documents)
            response = ollama.chat(model="qwen2", messages=[
                {"role": "user", "content": query},
                {"role": "system", "content": context}
            ])

            if 'message' in response and 'content' in response['message']:
                return response['message']['content']
            elif 'choices' in response and len(response['choices']) > 0:
                return response['choices'][0].get('text', "未能获得有效回复")
            else:
                return "未能获得有效回复"
        except Exception as e:
            return f"联网查询失败，错误信息：{e}"

    @staticmethod
    def search(query, documents):
        """查询过程：先查询文档内容，后查询联网"""
        # 1. 查询文档内容
        local_response = WebSearch.search_local(query, documents)
        if local_response != "抱歉，我没有找到相关的文档。":
            return local_response

        # 2. 如果本地没有，查询联网（Ollama 模型）
        return WebSearch.search_model(query, documents)
