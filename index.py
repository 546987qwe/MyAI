import streamlit as st

# 设置标题居中
st.markdown("""
<style>
.title-center {
    text-align: center;
    margin-bottom: 20px;
}
.st-emotion-cache-1kyxreq {
width: 200px;
}
.st-emotion-cache-1vt4y43 {
width: 200px;
}

.st-emotion-cache-1wmy9hl .e1f1d6gn5{
    width: 704px;
    position: absolute;
    top: 100%;
    }
.e115fcil2{
width=200;
}
.st-emotion-cache-1kyxreq {
padding-left: 12px;
}
.stButton {
width=200;
padding-left: 12px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
       <a href="http://book.free.svipss.top/#/root/"> <button type="button">书籍详情展示</button></a>
        <style>
        a button{
            position: absolute;
            top: 0px;
            left: 34%;
            width: 200px;
            border-radius: 8px;
            border-width:1px;
            border-color: rgb(49, 51, 63, 0.2);
            cursor: pointer;
            background-color:white;
        }
    </style>""", unsafe_allow_html=True)
# 生成居中的标题
st.markdown('<h1 class="title-center">欢迎来到我的AI</h1>', unsafe_allow_html=True)

# 创建列
c4, c5,c6= st.columns(3)
# c6= st.columns(1)[0]

#
# with c1:
#     st.image("images/img_1.png", use_column_width=True)
#     flag1 = st.button("初级", use_container_width=True)
#     if flag1:
#         st.switch_page("pages/job_vector1.py")
#
# with c2:
#     st.image("images/img_2.png", use_column_width=True)
#     flag2 = st.button("进阶1", use_container_width=True)
#     if flag2:
#         st.switch_page("pages/demo2.py")
#
# with c3:
#     st.image("images/img_3.png", use_column_width=True)
#     flag3 = st.button("进阶2", use_container_width=True)
#     if flag3:
#         st.switch_page("pages/demo3.py")

with c4:
    st.image("images/img_1.png", width=200)
    flag4 = st.button("全知")
    if flag4:
        st.switch_page("pages/demo4.py")

with c5:
    st.image("images/img_2.png", width=200)
    flag5 = st.button("图片生成")
    if flag5:
         st.switch_page("pages/image.py")
with c6:
    st.image("images/img_3.png",width=200)
    flag5 = st.button("书籍智能问答系统")
    if flag5:
        st.switch_page("pages/book_ai.py")
