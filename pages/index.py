import streamlit as st

# 设置标题居中
st.markdown("""
<style>
.title-center {
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# 生成居中的标题
st.markdown('<h1 class="title-center">欢迎来到我的AI</h1>', unsafe_allow_html=True)

# 创建列
c1, c2, c3, c4, c5 = st.columns(5)
c4, c5 = st.columns(2)

# with c1:
#     st.image("images/img_1.png", use_column_width=True)
#     flag1 = st.button("初级", use_container_width=True)
#     if flag1:
#         st.switch_page("pages/demo1.py")

# with c2:
#     st.image("images/img_2.png", use_column_width=True)
#     flag2 = st.button("进阶1", use_container_width=True)
#     if flag2:
#         st.switch_page("pages/demo1.py")

# with c3:
#     st.image("images/img_3.png", use_column_width=True)
#     flag3 = st.button("进阶2", use_container_width=True)
#     if flag3:
#         st.switch_page("pages/demo1.py")

with c4:
    st.image("images/img_4.png", use_column_width=True)
    flag4 = st.button("全知", use_container_width=True)
    if flag4:
        st.switch_page("pages/demo1.py")

with c5:
    st.image("images/img_5.png", use_column_width=True)
    flag5 = st.button("图片生成", use_container_width=True)
    if flag5:
        st.switch_page("pages/image.py")
