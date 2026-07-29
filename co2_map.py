## GeoJSON으로 서울 지도 데이터 가져오기

import geopandas as gpd

seoul = gpd.read_file("서울_자치구_경계_2017.geojson")

## 지도 그리는 함수
import folium
def draw_map(merged, month):

    m = folium.Map(
        location=[37.5665,126.9780],
        zoom_start=11
    )

    folium.Choropleth(
        geo_data=merged,
        data=merged,
        columns=["자치구명", month],
        key_on="feature.properties.SIG_KOR_NM",
        fill_color="YlOrRd",
        fill_opacity=0.8,
        line_opacity=0.2,
        legend_name=f"{month} CO₂ 배출량"
    ).add_to(m)

    return m

## 탄소가스 배출량 데이터 가져오기
## 데이터 출처 https://energyinfo.seoul.go.kr/energy/custEnergyUsage?menu-id=Z020700

import pandas as pd
from pathlib import Path
import streamlit as st
from streamlit_folium import st_folium

## streamlit으로 먼저 뼈대 만들기
st.title("서울 탄소 배출 지도")
year = st.selectbox(
    "년도",
    [2020,2021,2022,2023,2024,2025, 2026]
)
energy = st.selectbox(
    "에너지원",
    ["전기","가스","지역난방"]
)
month = st.selectbox(
    "월",
    ["1월","2월","3월","4월",
     "5월","6월","7월","8월",
     "9월","10월","11월","12월","1년 총합"]
)

## 데이터 로드
path = Path("온실가스 데이터")

df = pd.read_csv(path/f"{energy}_{year}.csv", skiprows=1)
df = df.rename(columns={"계": "1년 총합"})

## 데이터 다 float으로 바꾸기
cols_df = df.columns[2:15]

for col in cols_df:
    df[col] = pd.to_numeric(
        df[col].astype(str).str.replace(",", "", regex=False),
        errors="coerce"
    )  

## 지도 데이터와 합치기
merged = seoul.merge(
    df,
    left_on="SIG_KOR_NM",
    right_on="자치구명"
)    

## 지도 만들기(월별, 년별)
m = draw_map(merged, month)
 
st_folium(m, width=900, height=700)