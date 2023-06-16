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

# 배경 이미지 URL
background_image_url = 'http://front-end-noobs.com/jecko/img/wave-top.png'

# Streamlit 앱 설정
st.set_page_config(page_title='Streamlit 앱', layout='wide')

# 배경 이미지 적용
st.markdown(
    f"""
    <style>
    body {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 컨텐츠 표시
st.title('이것은 제목입니다')
st.write('이것은 내용입니다.')
