import streamlit as st

st.set_page_config(page_title="AI Art Generator", page_icon="🎨")

st.title("🎨 AI Art Generator")
st.write("환영합니다! 이것은 목사님과 김 전도사님의 첫 AI 신작 공동 프로젝트입니다.")

prompt = st.text_input("생성할 이미지를 설명해주세요:", "빛 가운데 서 있는 예수님")

if st.button("이미지 생성"):
    st.image("https://placehold.co/600x400?text=" + prompt, caption=prompt)
    st.success("AI 성화 생성이 완료되었습니다.")