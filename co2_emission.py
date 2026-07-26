import streamlit as st

st.title("🌱 탄소 절감 계산기")

# 1. 전기 절약
electric = st.checkbox("⚡ 전기 절약")
if electric:
    electric_amount = st.number_input(
        "절약한 전력(kWh)",
        min_value=0.0,
        step=0.1
    )

# 2. 버스 이용
bus = st.checkbox("🚌 자동차 대신 버스 타기")
if bus:
    bus_distance = st.number_input(
        "버스로 이동한 거리(km)",
        min_value=0.0,
        step=0.5
    )

# 3. 채식
vegan = st.checkbox("🥗 채식하기")
if vegan:
    vegan_meals = st.number_input(
        "채식한 횟수(끼)",
        min_value=0,
        step=1
    )

# 4. 재활용
recycle = st.checkbox("♻️ 재활용하기")
if recycle:
    recycle_count = st.number_input(
        "재활용한 개수",
        min_value=0,
        step=1
    )

if st.button("계산하기"):
    st.success("계산 기능은 다음 단계에서 추가!")