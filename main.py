"""
智能聊天机器人 - 主程序入口
功能：基于规则的聊天机器人，支持多种交互功能
"""

import streamlit as st
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from src.chat_logic import Chatbot
from config.settings import BOT_CONFIG

st.set_page_config(
    page_title="智能聊天机器人",
    page_icon="🤖",
    layout="wide"
)

if os.path.exists(os.path.join(current_dir, "assets", "style.css")):
    with open(os.path.join(current_dir, "assets", "style.css"), "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

chatbot = st.session_state.chatbot

st.title("🤖 智能聊天机器人")
st.markdown("小助手随时为你服务！")

with st.sidebar:
    st.header("📋 小助手")
    st.markdown(f"在线状态: <span style='color: green;'>● 在线</span>", unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("支持的功能:")
    functions = [
        "💬 聊天对话",
        "❓ 问答服务",
        "😄 讲笑话",
        "⏰ 时间查询",
        "📅 日期查询"
    ]
    for func in functions:
        st.write(func)
    
    if st.button("🗑️ 清空聊天记录"):
        chatbot.clear_history()
        st.success("聊天记录已清空！")

chat_container = st.container()

with chat_container:
    for message in chatbot.get_history():
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.markdown(f"""
                <div class="user-message">
                    <div class="message-bubble user">
                        {content}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="bot-message">
                    <div class="message-bubble bot">
                        {content}
                    </div>
                </div>
            """, unsafe_allow_html=True)

user_input = st.text_input("输入消息...", key="user_input", placeholder="请输入你的问题或消息...")

if st.button("发送", use_container_width=True):
    if user_input.strip():
        chatbot.add_message("user", user_input)
        
        response = chatbot.get_response(user_input)
        chatbot.add_message("assistant", response)
        
        try:
            st.rerun()
        except AttributeError:
            st.experimental_rerun()
    else:
        st.warning("请输入消息！")