"""加载税务文档到向量库"""
from src.vector_store import VectorStore
from src.config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    store = VectorStore()
    
    count = store.load_chunks_from_dir(Config.DATA_CHUNKS_DIR)
    
    print(f"\n✅ 加载完成！向量库共有 {store.get_count()} 个文档块")
    
    # 测试检索
    test_query = "个人所得税"
    docs, metas, scores = store.search(test_query)
    print(f"\n🔍 测试检索: {test_query}")
    print(f"找到 {len(docs)} 个相关文档")

if __name__ == "__main__":
    main()