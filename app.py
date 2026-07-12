import streamlit as st
import google.generativeai as genai
from PIL import Image

# ページ設定
st.title("英文解析アプリ")

# API設定
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# モデル設定（最新の標準仕様）
model = genai.GenerativeModel("gemini-1.5-flash")

# 画像アップロード
uploaded_file = st.file_uploader("画像を選択", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image)
    if st.button("解析実行"):
        try:
            response = model.generate_content(["添付画像を解析して", image])
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー内容: {e}")
