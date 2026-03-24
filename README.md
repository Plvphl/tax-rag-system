# 税务RAG问答系统

基于RAG（检索增强生成）的税务知识问答系统。

## 👥 加入项目

**邀请链接**：https://repocard.io/invite/github.com/Plvphl/tax-rag-system

点击上方链接申请加入项目协作者！

### 贡献指南
1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

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