import chromadb
from chromadb.utils import embedding_functions
from src.config import Config
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=Config.CHROMA_DIR)
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=Config.EMBEDDING_MODEL
        )
        self.collection = self.client.get_or_create_collection(
            name=Config.COLLECTION_NAME,
            embedding_function=self.embedding_fn
        )
        logger.info(f"向量库已就绪，现有文档数: {self.collection.count()}")
    
    def load_chunks_from_dir(self, chunks_dir):
        """加载税务分块文档"""
        if not os.path.exists(chunks_dir):
            logger.error(f"目录不存在: {chunks_dir}")
            return 0
        
        documents = []
        ids = []
        metadatas = []
        
        for filename in os.listdir(chunks_dir):
            if filename.endswith('.json'):
                filepath = os.path.join(chunks_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    chunks = json.load(f)
                
                for i, chunk in enumerate(chunks):
                    documents.append(chunk['text'])
                    ids.append(f"{filename}_{i}")
                    metadatas.append({'source': chunk.get('source', filename)})
            elif filename.endswith('.txt'):
                filepath = os.path.join(chunks_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                documents.append(text)
                ids.append(filename.replace('.txt', ''))
                metadatas.append({'source': filename})
        
        if documents:
            self.collection.add(
                documents=documents,
                ids=ids,
                metadatas=metadatas
            )
            logger.info(f"已加载 {len(documents)} 个文档块")
        
        return len(documents)
    
    def search(self, query, k=None):
        k = k or Config.TOP_K
        results = self.collection.query(query_texts=[query], n_results=k)
        return results['documents'][0], results['metadatas'][0], results['distances'][0]
    
    def get_count(self):
        return self.collection.count()