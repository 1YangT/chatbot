# 智能聊天机器人

基于 Streamlit 框架开发的规则式聊天机器人，支持多轮对话、聊天记录保存，界面模仿 ChatGPT 气泡风格。

## 技术栈

- Python 3.10+
- Streamlit 1.28+

## 功能特点

- 🤖 **本地规则式聊天** - 无需 API，基于意图匹配的本地聊天实现
- 💬 **多轮对话** - 支持连续对话，上下文保持
- 💾 **聊天记录保存** - 自动保存到本地 JSON 文件
- 🗑️ **清空功能** - 一键清空聊天记录
- 🎨 **ChatGPT 风格界面** - 模仿 ChatGPT 的气泡式聊天界面
- 🟢 **在线状态** - 显示机器人在线状态

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
streamlit run main.py
```

### 访问地址

- 本地访问：http://localhost:8501

## 项目结构

```
.
├── main.py                   # 主程序文件
├── requirements.txt          # 依赖包列表
├── .gitignore               # Git 忽略文件
├── config/
│   └── settings.py          # 配置文件
├── utils/
│   └── common.py            # 工具函数
├── src/
│   └── chat_logic.py        # 聊天逻辑
├── data/
│   └── intents.json         # 意图数据
└── assets/
    └── style.css            # 样式文件
```

## 支持的意图

- 问候、告别、感谢
- 名字、年龄、帮助
- 时间、日期、天气
- 开心、难过、笑话
- 夸奖、关于、爱
- 爱好、编程、美食、旅行

## 部署到 Streamlit Community Cloud

1. 登录 [Streamlit Community Cloud](https://share.streamlit.io/)
2. 点击 "New app"
3. 选择 GitHub 仓库：`1YangT/chatbot`
4. 分支：`main`
5. 主文件路径：`main.py`
6. 点击 "Deploy"

## 许可证

MIT License
