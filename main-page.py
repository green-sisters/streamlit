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

preset_colors = [
    ("Default light", ThemeColor(
        primaryColor="#ff4b4b",
        backgroundColor="#ffffff",
        secondaryBackgroundColor="#f0f2f6",
        textColor="#31333F",
    )),
    ("Default dark", ThemeColor(
        primaryColor="#ff4b4b",
        backgroundColor="#0e1117",
        secondaryBackgroundColor="#262730",
        textColor="#fafafa",
    )),
    ("Custom theme", ThemeColor(
        primaryColor="rgba(102, 234, 0, 0.73)",
        backgroundColor="rgba(102, 234, 0, 0.73)",
        secondaryBackgroundColor="rgba(102, 234, 0, 0.73)",
        textColor="rgba(102, 234, 0, 0.73)",
    )),
]

def get_config_theme_color():
    config_theme_primaryColor = st._config.get_option('theme.primaryColor')
    config_theme_backgroundColor = st._config.get_option('theme.backgroundColor')
    config_theme_secondaryBackgroundColor = st._config.get_option('theme.secondaryBackgroundColor')
    config_theme_textColor = st._config.get_option('theme.textColor')
    if (
        config_theme_primaryColor is not None and
        config_theme_backgroundColor is not None and
        config_theme_secondaryBackgroundColor is not None and
        config_theme_textColor is not None
    ):
        return ThemeColor(
            primaryColor=config_theme_primaryColor,
            backgroundColor=config_theme_backgroundColor,
            secondaryBackgroundColor=config_theme_secondaryBackgroundColor,
            textColor=config_theme_textColor,
        )

    return None

theme_from_initial_config = get_config_theme_color()
if theme_from_initial_config:
    preset_colors.append(("From the config", theme_from_initial_config))
