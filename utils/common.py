"""
工具函数模块
包含文件读写、文本处理等通用功能
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List

current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_intents(file_path: str = None) -> Dict:
    """
    加载意图数据
    
    Args:
        file_path: JSON 文件路径
        
    Returns:
        意图数据字典
    """
    if file_path is None:
        file_path = os.path.join(current_dir, "data", "intents.json")
    
    if not os.path.exists(file_path):
        return {}
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"加载意图数据失败: {e}")
        return {}


def save_chat_history(history: List[Dict], file_path: str = None) -> bool:
    """
    保存聊天记录
    
    Args:
        history: 聊天记录列表
        file_path: JSON 文件路径
        
    Returns:
        是否保存成功
    """
    if file_path is None:
        file_path = os.path.join(current_dir, "data", "chat_history.json")
    
    try:
        data = {
            "saved_at": datetime.now().isoformat(),
            "messages": history
        }
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存聊天记录失败: {e}")
        return False


def load_chat_history(file_path: str = None) -> List[Dict]:
    """
    加载聊天记录
    
    Args:
        file_path: JSON 文件路径
        
    Returns:
        聊天记录列表
    """
    if file_path is None:
        file_path = os.path.join(current_dir, "data", "chat_history.json")
    
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("messages", [])
    except Exception as e:
        print(f"加载聊天记录失败: {e}")
        return []


def tokenize(text: str) -> List[str]:
    """
    文本分词（简单版本）
    
    Args:
        text: 输入文本
        
    Returns:
        分词结果列表
    """
    # 去除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # 转换为小写
    text = text.lower()
    # 按空格分词
    tokens = text.split()
    return tokens


def normalize_text(text: str) -> str:
    """
    文本归一化
    
    Args:
        text: 输入文本
        
    Returns:
        归一化后的文本
    """
    text = text.strip()
    text = text.replace('，', ',').replace('。', '.').replace('！', '!').replace('？', '?')
    return text
