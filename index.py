import streamlit as st
#生成首页，距离顶部50%，居中显示欢迎来到我的ai

st.markdown("""
<style>
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
