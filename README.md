# 税务RAG问答系统

基于RAG（检索增强生成）的税务知识问答系统。

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt

# 配置API Key
cp .env.example .env
# 编辑.env文件，填入你的API Key

# 加载税务文档到向量库
python scripts/load_documents.py

# 运行问答
python scripts/run_query.py "个人所得税起征点是多少？"