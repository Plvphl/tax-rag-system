from flask import Flask, request, render_template_string, redirect, url_for
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# GitHub配置
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # 需要在.env中设置
REPO_OWNER = 'Plvphl'
REPO_NAME = 'tax-rag-system'

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>加入税务RAG项目</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .container {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 1.5rem;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: #555;
            font-weight: 500;
        }
        input[type="text"] {
            width: 100%;
            padding: 0.75rem;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
            transition: border-color 0.3s;
            box-sizing: border-box;
        }
        input[type="text"]:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 0.75rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        .success {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
            text-align: center;
        }
        .error {
            background: #f8d7da;
            color: #721c24;
            padding: 1rem;
            border-radius: 5px;
            margin-top: 1rem;
            text-align: center;
        }
        .info {
            text-align: center;
            color: #666;
            margin-top: 1rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 加入税务RAG项目</h1>
        <form method="POST">
            <div class="form-group">
                <label for="name">姓名：</label>
                <input type="text" id="name" name="name" required placeholder="请输入你的姓名">
            </div>
            <div class="form-group">
                <label for="student_id">学号：</label>
                <input type="text" id="student_id" name="student_id" required placeholder="请输入你的学号">
            </div>
            <button type="submit">申请加入项目</button>
        </form>
        {% if message %}
            <div class="success">
                {{ message }}
            </div>
        {% endif %}
        {% if error %}
            <div class="error">
                {{ error }}
            </div>
        {% endif %}
        <div class="info">
            提交后你将自动获得项目协作者权限
        </div>
    </div>
</body>
</html>
'''

def add_collaborator(username):
    """添加GitHub协作者"""
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/collaborators/{username}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.put(url, headers=headers)
    return response.status_code == 201

@app.route('/', methods=['GET', 'POST'])
def invite():
    if request.method == 'POST':
        name = request.form.get('name')
        student_id = request.form.get('student_id')

        if not name or not student_id:
            return render_template_string(HTML_TEMPLATE, error="请填写完整信息")

        # 这里可以添加验证逻辑，比如检查学号格式等
        # 暂时直接通过

        # 注意：这里需要用户提供GitHub用户名
        # 为了简化，我们可以让用户在表单中也输入GitHub用户名
        # 或者通过其他方式获取

        return render_template_string(HTML_TEMPLATE,
                                    error="请在表单中添加GitHub用户名字段，或者联系管理员手动添加")

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)