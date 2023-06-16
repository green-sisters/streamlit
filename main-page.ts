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

import { transparentize } from "color2k"
import { colors } from "src/theme/primitives/colors"

export default {
  ...colors,
  bgColor: colors.white,
  bodyText: colors.gray85,
  primary: colors.red70,
  disabled: colors.gray40,
  lightestGray: colors.gray20,
  lightGray: colors.gray30,
  gray: colors.gray60,
  darkGray: colors.gray70,
  red: colors.red80,
  blue: colors.blue80,
  green: colors.green80,
  yellow: colors.yellow80,
  // For this one, we use a specific color,
  // outside our standard color palette,
  // to ensure contrast is good enough for accessibility
  warning: "#926C05",
  warningBg: transparentize(colors.yellow70, 0.9),
  success: colors.green100,
  successBg: transparentize(colors.green70, 0.9),
  info: colors.blue100,
  infoBg: transparentize(colors.blue70, 0.9),
  danger: colors.red100,
  dangerBg: transparentize(colors.red80, 0.91),
}
