import streamlit as st

st.title("🌱 탄소 절감 계산기")

actions = {
    "electric": {
        "label": "⚡ 전기 절약",
        "items": {
            "air": {
                "label": "에어컨",
                "unit": "시간",
                "factor": 0.8
            },
            "tv": {
                "label": "TV",
                "unit": "시간",
                "factor": 0.1
            },
            "light": {
                "label": "조명",
                "unit": "시간",
                "factor": 0.01
            },
            "computer": {
                "label": "컴퓨터",
                "unit": "시간",
                "factor": 0.02
            }
        }
    },

    "trans": {
        "label": "🚗 운송",
        "items": {
            "car": {
                "label": "자동차(휘발유)",
                "unit": "km",
                "factor": 0.02
            },
            "car_2": {
                "label": "자동차(경유)",
                "unit": "km",
                "factor": 0.02
            },
            "plane": {
                "label": "비행기",
                "unit": "시간",
                "factor": 0.03
            }
        }
    },

    "meal": {
        "label": "🥗 채식",
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