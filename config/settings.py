"""
配置文件
包含聊天机器人的页面设置和主题配置
"""

# 页面配置
PAGE_CONFIG = {
    "page_title": "智能聊天机器人",
    "page_icon": "🤖",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# 机器人配置
BOT_CONFIG = {
    "name": "小助手",
    "avatar": "🤖",
    "welcome_message": "你好！我是你的智能聊天助手，有什么可以帮助你的吗？",
    "default_response": "抱歉，我不太理解你的意思。你可以问我一些其他问题。"
}

# 用户配置
USER_CONFIG = {
    "name": "用户",
    "avatar": "👤"
}

# 数据文件路径
INTENTS_FILE = "data/intents.json"
CHAT_HISTORY_FILE = "data/chat_history.json"

# 主题颜色
THEME_COLORS = {
    "primary": "#3b82f6",
    "bot_bubble": "#f1f5f9",
    "user_bubble": "#3b82f6",
    "bot_text": "#1e293b",
    "user_text": "#ffffff"
}
