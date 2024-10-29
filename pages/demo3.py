# 制作聊天界面
import streamlit as st
from langchain_openai import ChatOpenAI
import json
# 引入提示词对象
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 构建大模型 智谱
model = ChatOpenAI(
    temperature=0.8,  # 创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="9ee0c01ef679f3b2d14f1d2e25f5371a.FZvJ83u5XiL3KJmJ",
)
# 创建提示词对象
prompt = PromptTemplate.from_template("你的名字叫小慧，你现在要扮演全知，你的性格是谨慎冷漠的，你现在要和向你寻求帮助的人交谈，你只需要回答他们的问题，不要和他们说有关具体提问，他们说的是{input}")
chain = LLMChain(llm=model, prompt=prompt)
st.title("李文慧 ChatOpenAI")

if "cache1" not in st.session_state:
    st.session_state.cache1 = []
else:
    for message in st.session_state.cache1:
       with st.chat_message(message['role']):
          st.write(message["content"])

# 创建聊天输入框
problem = st.chat_input("请输入你的问题")

# 确定问题被输入
if problem:
    # 输入问题、调用大模型回答问题、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
        st.write("思考中...")
    # 将用户消息添加到缓存
    st.session_state.cache1.append({"role": "user", "content": problem})
    # 调用大模型获取回答
    result = chain.invoke(problem)
    # 将大模型的回答添加到缓存
    with st.chat_message("assistant"):
        st.write("思考完成")
        st.write(result['text'])
    st.session_state.cache1.append({"role": "assistant", "content": result['text']})
