#!/bin/bash

# 邀请系统部署脚本

echo "🚀 部署税务RAG项目邀请系统"

# 检查是否安装了依赖
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 安装依赖
echo "📦 安装依赖..."
pip3 install -r invite_system/requirements.txt

# 检查.env文件
if [ ! -f ".env" ]; then
    echo "❌ .env 文件不存在，请创建并配置 GITHUB_TOKEN"
    echo "请在 .env 中添加：GITHUB_TOKEN=your_token_here"
    exit 1
fi

# 检查GITHUB_TOKEN
if ! grep -q "GITHUB_TOKEN" .env; then
    echo "❌ GITHUB_TOKEN 未在 .env 中配置"
    exit 1
fi

echo "✅ 环境检查通过"

# 启动应用
echo "🌟 启动邀请系统..."
echo "访问地址: http://localhost:5000"
cd invite_system && python3 app.py