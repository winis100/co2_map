import streamlit as st
import os

st.title("🌱 탄소 절감 결과")

# image_path = os.path.join(
#     os.path.dirname(__file__),
#     "..",
#     "house.png"
# )

# st.image(image_path, use_container_width=True)

if "result" not in st.session_state:
    st.warning("먼저 탄소 절감량을 계산해주세요.")
    st.stop()


result = st.session_state["result"]


total = result["total"]
electric = result["electric"]
replacement = result["replacement"]
recycle = result["recycle"]


st.metric(
    label="총 탄소 절감량",
    value=f"{total:.2f} kgCO₂"
)


st.divider()


st.subheader("분야별 절감량")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "⚡ 전기 절약",
        f"{electric:.2f} kgCO₂"
    )

with col2:
    st.metric(
        "🍚 식사·이동 변화",
        f"{replacement:.2f} kgCO₂"
    )

with col3:
    st.metric(
        "♻️ 재활용",
        f"{recycle:.2f} kgCO₂"
    )

if st.button("🌳 절감 효과 확인", type="primary"):
    st.switch_page("pages/effect.py")