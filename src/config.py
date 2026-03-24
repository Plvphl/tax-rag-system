import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # 数据路径
    DATA_CHUNKS_DIR = "data/chunks"
    
    # 向量库
    CHROMA_DIR = "chroma_data"
    COLLECTION_NAME = "tax_docs"
    
    # Embedding模型
    EMBEDDING_MODEL = "BAAI/bge-small-zh"
    
    # RAG配置
    TOP_K = 3
    
    # LLM API
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "deepseek")
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")