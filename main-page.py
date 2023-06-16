# # mobile layout ##############################################################################################################
# # 색상: rgba(102, 234, 0, 0.73) (=#66ea00;), 크기 조정

# import streamlit as st

# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: linear-gradient(rgba(102, 234, 0, 0.73), rgba(102, 234, 0, 0.03));
#         background-size: cover;
#     }
#     @media (max-width: 600px) {
#         .reportview-container .markdown-text-container {
#             font-size: 16px;
#         }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title('This is a title')
# st.write('This is some content.')

import streamlit as st

# CSS 코드
css = """
<style>
.reportview-container {
    background: linear-gradient(rgba(102, 234, 0, 0.73), rgba(102, 234, 0, 0.03));
    background-size: cover;
}
@media (max-width: 600px) {
    .reportview-container .markdown-text-container {
        font-size: 16px;
    }
}
</style>
"""

# Streamlit 앱 설정
st.set_page_config(page_title='모바일 레이아웃', layout='wide')

# CSS 코드 적용
st.markdown(css, unsafe_allow_html=True)

# 타이틀 및 내용 표시
st.title('이것은 제목입니다')
st.write('이것은 내용입니다.')


