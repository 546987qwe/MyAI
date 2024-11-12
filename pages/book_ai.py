import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.utilities  import SQLDatabase
from langchain.chains import LLMChain,create_sql_query_chain
from langchain.prompts import PromptTemplate

st.title("书籍智能问答系统")
st.markdown("""
       <a  href="http://zq5xpg.natappfree.cc/#/"><button type="button" class="a">书籍详情展示</button></a>
        <style>
        .a {
            position: absolute;
            bottom: 25px;
            left: 80%;
            width: 200px;
            border-radius: 8px;
            border-width:1px;
            border-color: rgb(49, 51, 63, 0.2);
            background-color:white;
        }
    </style>""", unsafe_allow_html=True)

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for mess in st.session_state.cache:
        with st.chat_message(mess["role"]):
            st.write(mess["content"])
db=SQLDatabase.from_uri("mysql+pymysql://books:books@server.natappfree.cc:46589/books")
mode=ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key="56e1ba13787686b2f729a2c7028025b6.zUNI18EwnjVc8e3D",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
sql_chain=create_sql_query_chain(llm=mode,db=db)
prompt=PromptTemplate.from_template(
    "现在你是一个专业的数据库问答专家，你只能对数据库的这些问题做回答，用户的提问是{input},数据库对问题的回答是{answer},你需要对数据库的回答加以美化，以人的说话的口吻输出结果"
)
bean_chain=LLMChain(llm=mode,prompt=prompt)
problem=st.chat_input("请输入问题：")

if problem:
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.cache1.append({"role":"user","content":problem})
    sql=sql_chain.invoke({"question":problem})
    if 'SELECT' in sql:
        first=sql.index("SELECT")
        end_index=sql.find(";",first+1)
        sql=sql[first:end_index+1]
        print("sql:",sql)
        try:
            result=db.run(sql)
            bean_result=bean_chain.invoke({
                "input":problem,
                "answer":result,})
            with st.chat_message("assistant"):
                st.write(bean_result["text"])
            st.session_state.cache1.append({"role":"assistant","content":bean_result["text"]})
        except:
            bean_result = bean_chain.invoke({
                "input": problem,
                "answer": "出错了，请重新提问",
            })
            with st.chat_message("assistant"):
                st.write(bean_result["text"])
            st.session_state.cache.append({"role": "assistant", "content": bean_result["text"]})
    elif "select" in sql:
        first = sql.index("select")
        end_index = sql.find(";", first + 1)
        sql = sql[first:end_index + 1]
        print("sql:", sql)
        try:
            result = db.run(sql)
            bean_result = bean_chain.invoke({
                "input": problem,
                "answer": result, })
            with st.chat_message("assistant"):
                st.write(bean_result["text"])
            st.session_state.cache.append({"role": "assistant", "content": bean_result["text"]})
        except:
            bean_result = bean_chain.invoke({
                "input": problem,
                "answer": "出错了，请重新提问",
            })
            with st.chat_message("assistant"):
                st.write(bean_result["text"])
            st.session_state.cache.append({"role": "assistant", "content": bean_result["text"]})
    else:
        bean_result = bean_chain.invoke({
            "input": problem,
            "answer": sql,
        })
        with st.chat_message("assistant"):
            st.write(bean_result["text"])
        st.session_state.cache.append({"role": "assistant", "content": bean_result["text"]})



