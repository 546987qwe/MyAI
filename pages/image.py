from zhipuai import ZhipuAI
import streamlit as st

st.title("AI绘画")
client = ZhipuAI(api_key="9ee0c01ef679f3b2d14f1d2e25f5371a.FZvJ83u5XiL3KJmJ")  # 请填写您自己的APIKey

if "cache3" not in st.session_state:
    st.session_state.cache3 = []
else:
    for message in st.session_state.cache3:
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
    st.session_state.cache3.append({"role": "user", "content": description})
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
                st.session_state.cache3.append({"role": "assistant", "content": image_data.url})
            else:
                st.write("生成的图片失败")
        else:
            st.write("生成的图片失败")
    except Exception as e:
        st.write(f"发生错误: {e}")
