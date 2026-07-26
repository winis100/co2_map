import streamlit as st

st.title("🌱 탄소 절감 계산기")

actions = {
    "electric": {
        "label": "⚡ 전기 절약",
        "emission_factor": 414.9,
        "items": {
            "air": {
                "label": "에어컨",
                "unit": "시간",
                "factor": 1.3
            },
            "tv": {
                "label": "TV",
                "unit": "시간",
                "factor": 0.12
            },
            "light": {
                "label": "조명",
                "unit": "시간",
                "factor": 0.03
            },
            "laptop": {
                "label": "노트북",
                "unit": "시간",
                "factor": 0.025
            }
        }
    },

    "trans": {
        "label": "🚗 운송",
        "emission_factor": 1,
        "items": {
            "car": {
                "label": "자동차(휘발유)",
                "unit": "L",
                "factor": 19.731
            },
            "car_2": {
                "label": "자동차(경유)",
                "unit": "L",
                "factor": 20.090
            },
            "plane": {
                "label": "비행기",
                "unit": "시간",
                "factor": 900 * 285
            }
        }
    },

    "meal": {
        "label": "🥗 채식",
        "emission_factor": 1,
        "items": {
            "beef": {
                "label": "소고기",
                "unit": "g",
                "factor": 0.03
            },
            "pork": {
                "label": "돼지고기",
                "unit": "g",
                "factor": 0.01
            },
            "lamp": {
                "label": "양",
                "unit": "g",
                "factor": 0.02
            },
            "chicken": {
                "label": "닭",
                "unit": "g",
                "factor": 0.01
            }
        }
    },

    "recycle": {
        "label": "♻️ 재활용",
        "emission_factor": 1,
        "items": {
            "can": {
                "label": "캔",
                "unit": "개",
                "factor": 0.02
            },
            "plastic_bottle": {
                "label": "플라스틱 병",
                "unit": "병",
                "factor": 0.02
            }
        }
    }
}

selected_actions = {}

for category_key, category_info in actions.items():

    if st.checkbox(category_info["label"]):

        for item_key, item_info in category_info["items"].items():

            if st.checkbox(item_info["label"]):

                value = st.number_input(
                    f"{item_info['label']} ({item_info['unit']})",
                    min_value=0.0,
                    step=1.0,
                    key=f"value_{category_key}_{item_key}"
                )

                selected_actions[item_key] = {
                    "value": value,
                    "factor": item_info["factor"],
                    "emission_factor": category_info["emission_factor"],
                    "label": item_info["label"],
                    "unit": item_info["unit"]
                }

if st.button("계산하기"):
    total = 0

    for action in selected_actions.values():
        total += action["value"] * action["factor"] * action["emission_factor"]

    st.success(f"총 탄소 절감량 : {total:.2f} kgCO₂")