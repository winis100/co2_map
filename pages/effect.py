import streamlit as st
import os

st.title("🌳 탄소 절감 효과")

if "result" not in st.session_state:
    st.warning("먼저 탄소 절감량을 계산해주세요.")
    st.stop()

result = st.session_state["result"]

total = result["total"]

tree10 = total / 1.4
tree40 = total / 9.0

base_path = os.path.dirname(os.path.dirname(__file__))

image_path1 = os.path.join(
    base_path,
    "10years_one.png"
)

image_path2 = os.path.join(
    base_path,
    "10years_multi.png"
)

image_path3 = os.path.join(
    base_path,
    "40years_one.png"
)

image_path4 = os.path.join(
    base_path,
    "40years_multi.png"
)

st.subheader("🌳 탄소 절감 효과")

st.markdown(
    f"이번 실천으로 절감한 **{total:.2f} kgCO₂**는\n\n"
    "소나무의 연간 CO₂ 흡수량으로 환산하면 다음과 같습니다."
)

col1, col2 = st.columns(2)

with col1:

    if tree10 >= 1:
        st.image(
            image_path1,
            use_container_width=True
        )
    else:
        st.image(
            image_path2,
            use_container_width=True
        )

    st.markdown("### 🌱 10임령")
    st.metric(
        "환산 결과",
        f"{tree10:.1f} 그루"
    )
    st.caption("연간 CO₂ 흡수량 기준")

with col2:

    if tree40 >= 1:
        st.image(
            image_path3,
            use_container_width=True
        )
    else:
        st.image(
            image_path4,
            use_container_width=True
        )

    st.markdown("### 🌲 40임령")
    st.metric(
        "환산 결과",
        f"{tree40:.1f} 그루"
    )
    st.caption("연간 CO₂ 흡수량 기준")