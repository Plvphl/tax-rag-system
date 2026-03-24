from src.vector_store import VectorStore
from src.config import Config
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGPipeline:
    def __init__(self):
        self.vector_store = VectorStore()
    
    def _call_llm(self, prompt):
        """调用LLM API"""
        if Config.LLM_PROVIDER == "deepseek":
            headers = {
                "Authorization": f"Bearer {Config.DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1
            }
            response = requests.post(
                f"{Config.DEEPSEEK_BASE_URL}/v1/chat/completions",
                headers=headers,
                json=data
            )
            return response.json()["choices"][0]["message"]["content"]
        else:
            return "请配置LLM_API"
    
    def query(self, question):
        """执行RAG问答"""
        # 检索
        documents, metadatas, scores = self.vector_store.search(question)
        
        # 构建prompt
        context = "\n\n---\n\n".join(documents)
        prompt = f"""你是一个专业的税务助手。请基于以下税务文档回答问题。
如果文档中没有相关信息，请说"根据现有文档无法回答这个问题"。

【文档内容】
{context}

【问题】
{question}

【回答】
"""
        
        # 生成回答
        answer = self._call_llm(prompt)
        
        return {
            "question": question,
            "answer": answer,
            "sources": [m.get('source', 'unknown') for m in metadatas]
        }