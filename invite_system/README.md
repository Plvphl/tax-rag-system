# 邀请系统使用说明

## 功能
- 成员填写姓名、学号和GitHub用户名
- 自动添加到GitHub仓库协作者
- 美观的Web界面

## 部署步骤

### 1. 配置GitHub Token
在项目根目录的 `.env` 文件中添加：
```
GITHUB_TOKEN=your_github_personal_access_token
```

### 2. 获取GitHub Token
1. 访问 https://github.com/settings/tokens
2. 生成新的Personal Access Token
3. 选择权限：`repo` (全选)

### 3. 运行应用
```bash
cd invite_system
pip install -r requirements.txt
python app.py
```

### 4. 访问
打开浏览器访问 `http://localhost:5000`

## 部署到生产环境
推荐部署到：
- Vercel (免费)
- Heroku
- Railway
- Render

## 安全注意事项
- Token要妥善保管，不要提交到代码中
- 生产环境使用环境变量存储Token
- 可以添加更多的验证逻辑（如学号格式检查）