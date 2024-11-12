from zhipuai import ZhipuAI
import streamlit as st

st.title("AI绘画")
st.markdown("""
       <a  href="http://book.free.svipss.top/#/root/"><button type="button" class="a">书籍详情展示</button></a>
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

client = ZhipuAI(api_key="56e1ba13787686b2f729a2c7028025b6.zUNI18EwnjVc8e3D")  # 请填写您自己的APIKey

if "cache2" not in st.session_state:
    st.session_state.cache2= []
else:
  for message in st.session_state.cache2:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.image(message["content"], width=200)
description = st.chat_input("请输入图片描述")
if description:
    with st.chat_message("user"):
        st.write(description)
        st.write("正在生成图片")
    st.session_state.cache2.append({"role": "user", "content": description})
    try:
        response = client.images.generations(
            model="cogview-3-plus",  # 填写需要调用的模型编码
            prompt=description,
        )
        if response and response.data and len(response.data) > 0:
            image_data = response.data[0]
            if image_data.url:
                with st.chat_message("assistant"):
                    st.image(image_data.url, width=300)
                    # 将图片url写入cache
                st.session_state.cache2.append({"role": "assistant", "content": image_data.url})
            else:
                st.write("生成的图片失败")
        else:
            st.write("生成的图片失败")
    except Exception as e:
        st.write(f"发生错误: {e}")
