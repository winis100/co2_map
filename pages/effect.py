import streamlit as st

st.title("🌳 탄소 절감 효과")

if "result" not in st.session_state:
    st.warning("먼저 탄소 절감량을 계산해주세요.")
    st.stop()

result = st.session_state["result"]

total = result["total"]

tree10 = total / 1.4
tree40 = total / 9.0

st.write(
    f"""
이번 실천으로 절감한 **{total:.2f} kgCO₂**는

🌱 **10임령 소나무 약 {tree10:.1f}그루**

또는

🌲 **40임령 소나무 약 {tree40:.1f}그루**

가 1년 동안 흡수하는 이산화탄소와 비슷한 양입니다.
"""
)

if st.button("← 결과 페이지로 돌아가기"):
    st.switch_page("pages/result.py")