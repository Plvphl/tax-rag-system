"""命令行问答"""
from src.rag_pipeline import RAGPipeline
import sys

def main():
    rag = RAGPipeline()
    
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        result = rag.query(question)
        print(f"\n问题: {result['question']}")
        print(f"回答: {result['answer']}")
        print(f"来源: {', '.join(result['sources'])}")
    else:
        print("税务RAG问答系统")
        print("使用方法: python scripts/run_query.py '你的问题'")

if __name__ == "__main__":
    main()