import streamlit as st

# 确保文件路径正确
video_path = '自动化批量爬取网页内容.mp4'

# 使用相对路径或绝对路径读取视频文件
try:
    with open(video_path, 'rb') as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)
except FileNotFoundError:
    st.error("视频文件未找到，请检查文件路径是否正确。")
