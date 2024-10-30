import streamlit as st

pages = {
    "首页": [
        st.Page("pages/index.py", title="首页"),
    ],
    # "初级": [
    #     st.Page("pages/demo1.py", title="初级"),
    # ],
    # "进阶1": [
    #     st.Page("pages/demo2.py", title="进阶"),
    # ],
    # "进阶2": [
    #     st.Page("pages/demo3.py", title="加强"),
    # ],
    "全知": [
        st.Page("pages/demo4.py", title="全知"),
    ],
    "图片生成": [
        st.Page("pages/image.py", title="图片生成"),
    ],
}
pg = st.navigation(pages)
pg.run()
