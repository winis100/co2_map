import streamlit as st

st.title("🌱 탄소 절감 결과")


if "total" in st.session_state:

    total = st.session_state["total"]

    st.metric(
        "총 탄소 절감량",
        f"{total*1000:.2f} kgCO₂"
    )

else:

    st.warning("계산 결과가 없습니다.")