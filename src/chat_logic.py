"""
聊天逻辑模块
包含规则式聊天的核心逻辑
"""

import random
import re
from typing import Dict, List
from utils.common import load_intents
from config.settings import BOT_CONFIG


class Chatbot:
    """
    聊天机器人类
    基于规则的本地聊天实现
    """
    
    def __init__(self):
        """初始化聊天机器人"""
        self.intents = load_intents()
        self.chat_history = []
    
    def add_message(self, role: str, content: str):
        """
        添加消息到聊天历史
        
        Args:
            role: 角色（user 或 assistant）
            content: 消息内容
        """
        self.chat_history.append({
            "role": role,
            "content": content
        })
    
    def get_response(self, user_input: str) -> str:
        """
        获取机器人响应
        
        Args:
            user_input: 用户输入
            
        Returns:
            机器人响应
        """
        # 查找匹配的意图
        response = self._match_intent(user_input)
        
        if response:
            return response
        
        # 如果没有匹配到意图，尝试关键词匹配
        response = self._match_keyword(user_input)
        
        if response:
            return response
        
        # 返回默认响应
        return BOT_CONFIG["default_response"]
    
    def _match_intent(self, user_input: str) -> str:
        """
        意图匹配
        
        Args:
            user_input: 用户输入
            
        Returns:
            响应文本（如果匹配到），否则返回 None
        """
        user_input_lower = user_input.lower().strip()
        
        for intent in self.intents.get("intents", []):
            patterns = intent.get("patterns", [])
            responses = intent.get("responses", [])
            
            for pattern in patterns:
                pattern_lower = pattern.lower()
                
                # 精确匹配或包含匹配
                if pattern_lower in user_input_lower or user_input_lower in pattern_lower:
                    # 随机选择一个响应
                    return random.choice(responses)
                
                # 正则匹配
                try:
                    if re.search(pattern_lower, user_input_lower):
                        return random.choice(responses)
                except:
                    pass
        
        return None
    
    def _match_keyword(self, user_input: str) -> str:
        """
        关键词匹配
        
        Args:
            user_input: 用户输入
            
        Returns:
            响应文本（如果匹配到），否则返回 None
        """
        user_input_lower = user_input.lower().strip()
        
        # 问候类关键词
        greetings = ["你好", "hello", "hi", "您好", "嗨", "哈喽"]
        if any(g in user_input_lower for g in greetings):
            return random.choice([
                "你好！很高兴见到你！",
                "Hi！有什么可以帮你的吗？",
                "你好呀！😊"
            ])
        
        # 感谢类关键词
        thanks = ["谢谢", "thank", "感谢", "辛苦了"]
        if any(t in user_input_lower for t in thanks):
            return random.choice([
                "不客气！这是我应该做的！",
                "不用谢！很高兴能帮到你！",
                "😊 随时为你服务！"
            ])
        
        # 再见类关键词
        goodbyes = ["再见", "bye", "拜拜", "下次见"]
        if any(g in user_input_lower for g in goodbyes):
            return random.choice([
                "再见！祝你有美好的一天！",
                "Bye！期待下次见面！",
                "再见！随时欢迎回来！"
            ])
        
        # 星期查询（放在日期查询前面，避免"今天"被先匹配）
        week_keywords = ["星期", "周几", "礼拜"]
        has_week = any(w in user_input_lower for w in week_keywords)
        if has_week:
            from datetime import datetime
            week_days = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
            now = datetime.now()
            return f"今天是 {week_days[now.weekday()]}"
        
        # 时间查询
        time_keywords = ["时间", "几点"]
        has_time = any(t in user_input_lower for t in time_keywords)
        if has_time:
            from datetime import datetime
            now = datetime.now()
            return f"现在是 {now.strftime('%H:%M')}"
        
        # 日期查询
        date_keywords = ["日期", "今天", "几号"]
        has_date = any(d in user_input_lower for d in date_keywords)
        if has_date and not has_week and not has_time:
            from datetime import datetime
            now = datetime.now()
            return f"今天是 {now.strftime('%Y年%m月%d日')}"
        
        # 天气查询
        weather_keywords = ["天气", "气温", "下雨", "晴天"]
        if any(w in user_input_lower for w in weather_keywords):
            return random.choice([
                "抱歉，我目前无法查询实时天气，请查看天气应用！",
                "天气信息需要联网查询，建议使用天气APP！"
            ])
        
        return None
    
    def clear_history(self):
        """清空聊天历史"""
        self.chat_history = []
    
    def get_history(self) -> List[Dict]:
        """
        获取聊天历史
        
        Returns:
            聊天历史列表
        """
        return self.chat_history
