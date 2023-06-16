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

from streamlit.theme import Theme

colors = {
    "white": "#ffffff",
    "gray20": "#333333",
    "gray30": "#666666",
    "gray60": "#999999",
    "gray70": "#b3b3b3",
    "gray85": "#d9d9d9",
    "red70": "#ff4b4b",
    "blue70": "#4b4bff",
    "blue80": "#3333ff",
    "green80": "#33cc33",
    "yellow80": "#cccc00",
    "yellow110": "#ffcc00",
    "red100": "#ff0000",
    "red80": "#ff3333",
    "green100": "#00ff00",
    "green80": "#33cc33",
    "blue100": "#0000ff"
}

theme = Theme(
    bgColor=colors["white"],
    secondaryBg=colors["gray20"],
    bodyText=colors["gray85"],
    warning=colors["yellow110"],
    warningBg=colors["yellow80"],
    success=colors["green100"],
    successBg=colors["green80"],
    infoBg=colors["blue70"],
    info=colors["blue100"],
    danger=colors["red100"],
    dangerBg=colors["red80"],
    primary=colors["red70"],
    disabled=colors["gray60"],
    lightestGray=colors["gray20"],
    lightGray=colors["gray30"],
    gray=colors["gray60"],
    darkGray=colors["gray70"],
    red=colors["red80"],
    blue=colors["blue80"],
    green=colors["green80"],
    yellow=colors["yellow80"]
)

# Streamlit 앱 설정
st.set_theme(theme)

