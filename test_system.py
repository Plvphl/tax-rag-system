#!/usr/bin/env python3
"""
测试脚本：验证所有模块是否正常工作
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """测试所有导入"""
    try:
        print("Testing imports...")
        import src.config
        print("✓ config module imported")

        import src.vector_store
        print("✓ vector_store module imported")

        import src.rag_pipeline
        print("✓ rag_pipeline module imported")

        print("\n🎉 All modules imported successfully!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_config():
    """测试配置"""
    try:
        from src.config import Config
        print(f"✓ Config loaded - LLM Provider: {Config.LLM_PROVIDER}")
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

if __name__ == "__main__":
    print("=== Tax RAG System Test ===\n")

    success = True
    success &= test_imports()
    success &= test_config()

    if success:
        print("\n✅ All tests passed! The system is ready to use.")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        sys.exit(1)