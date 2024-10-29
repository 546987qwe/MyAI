import streamlit as st
#生成首页，距离顶部50%，居中显示欢迎来到我的ai

st.markdown("""
<style>
body {
    background-image: url('https://img1.baidu.com/it/u=540965161,1553861445&fm=253&fmt=auto&app=120&f=JPEG?w=1280&h=800');
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
.center {
    position: relative;
    top:100px;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <div class="center">
        <h1 style="font-size: 50px;">欢迎来到我的AI</h1>
    </div>
    """,
    unsafe_allow_html=True
)
