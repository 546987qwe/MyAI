import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

#构建大模型 智谱
model=ChatOpenAI(
    temperature=0.8,#创新性
    model="glm-4-plus",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
    api_key="e210867e75503a51d642ec7f809cab2f.pNhLRYP2pdFLfjuJ",#
)
ConversationBuffer = ConversationBufferMemory()
if "memory" not in st.session_state:
    st.session_state.memory=ConversationBufferMemory(memory_key="history")
prompt=PromptTemplate.from_template("你的名字叫小慧，你现在要扮演全知，你的性格是谨慎冷漠的，你现在要和向你寻求帮助的人交谈，你只需要回答他们的问题，不要和他们说有关具体提问，他们说的是{input},你和他们的历史对话为{history}")
chain=LLMChain(
    llm=model,
    prompt=prompt,
    memory=st.session_state.memory,
)
st.title("李文慧 ChatOpenAI")
if "cache" not in st.session_state:
    st.session_state.cache = []
for message in st.session_state.cache:
        with st.chat_message(message['role']):
            st.write(message['content'])
# 创建聊天输入框
problem = st.chat_input("请输入你的问题")
#确定问题被输入
if problem:
#输入问题 、调用大模型回答问题 、将大模型回答的问题输出
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache.append({"role":"user","content":problem})
    result=chain.invoke({"input":problem})
    with st.chat_message("assistant"):
        st.write(result['text'])
    st.session_state.cache.append({"role":"assistant","content":result['text']})