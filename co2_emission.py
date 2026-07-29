import streamlit as st

st.title("🌱 탄소맵")

living_room = {
    "air": {
        "label": "에어컨",
        "unit": "분",
        "factor": 1.3 #kw 단위
    },
    "tv": {
        "label": "TV",
        "unit": "분",
        "factor": 0.12
    },
    "light": {
        "label": "조명",
        "unit": "분",
        "factor": 0.03
    },
    "cleaner": {
        "label": "청소기",
        "unit": "분",
        "factor": 0.6
    },
    "fan": {
        "label": "선풍기",
        "unit": "분",
        "factor": 0.05
    }
}

kitchen = {
    "cooker": {
        "label": "전기밥솥",
        "unit": "분",
        "factor": 1
    },
    "refri": {
        "label": "냉장고",
        "unit": "분",
        "factor": 0.1
    },
    "refri_k": {
        "label": "김치냉장고",
        "unit": "분",
        "factor": 0.3
    },
    "microwave": {
        "label": "전자레인지",
        "unit": "분",
        "factor": 0.8
    },
    "coffe_pot": {
        "label": "커피포트",
        "unit": "분",
        "factor": 0.7
    }
}

laundry_room = {
    "washing_machine": {
        "label": "세탁기",
        "unit": "분",
        "factor": 0.2
    },
    "iron": {
        "label": "다리미",
        "unit": "분",
        "factor": 1.2
    }
}

recycle = { # 단위 = tCO2eq/t
    "can": {
        "label": "캔",
        "unit": "개",
        "factor": 9.6
    },
    "glass": {
        "label": "유리병",
        "unit": "병",
        "factor": 1.2
    },
    "plastic": {
        "label": "플라스틱",
        "unit": "병",
        "factor": 0.3
    }
}

rooms = {
    "거실": living_room,
    "주방": kitchen,
    "다용도실": laundry_room,
    "재활용": recycle,
}

meal = {
    "beef": {
        "label": "소고기",
        "unit": "g",
        "factor": 100
    },
    "pork": {
        "label": "돼지고기",
        "unit": "g",
        "factor": 12
    },
    "chicken": {
        "label": "닭고기",
        "unit": "g",
        "factor": 7
    },
    "seafood": {
        "label": "해산물",
        "unit": "g",
        "factor": 5
    },
    "vegetarian_diet": {
        "label": "채식",
        "unit": "g",
        "factor": 1
    }
}

transportation = {
    "sub": {
        "label": "지하철",
        "unit": "km",
        "factor": 0.041
    },
    "bus": {
        "label": "버스",
        "unit": "km",
        "factor": 0.089
    },
    "gas": {
        "label": "휘발유차",
        "unit": "km",
        "factor": 0.192
    },
    "disel": {
        "label": "경유차",
        "unit": "km",
        "factor": 0.21
    },
    "lpg": {
        "label": "LPG차",
        "unit": "km",
        "factor": 0.197
    },
    "hybrid": {
        "label": "하이브리드차",
        "unit": "km",
        "factor": 0.1
    },
    "electric": {
        "label": "전기차",
        "unit": "km",
        "factor": 0.044
    }
}

electric = {}

electric.update(living_room)
electric.update(kitchen)
electric.update(laundry_room)

def create_inputs():

    user_inputs = {}

    for room_name, room in rooms.items():

        st.header(room_name)

        for key, info in room.items():

            user_inputs[key] = st.number_input(
                f'{info["label"]} ({info["unit"]})',
                min_value=0,
                key=key
            )

    return user_inputs

def create_replacement():

    user_inputs = {}

    st.header("식사")

    meal_labels = {
        info["label"]: key
        for key, info in meal.items()
    }

    col1, col2, col3 = st.columns(3)
    with col1:
        selected = st.selectbox(
            "평소식단",
            meal_labels.keys()
        )
        user_inputs["평소식단"] = meal_labels[selected]

    with col2:
        selected = st.selectbox(
            "오늘식단",
            meal_labels.keys()
        )
        user_inputs["오늘식단"] = meal_labels[selected]

    with col3:
        user_inputs["섭취량"] = st.number_input(
            "섭취량(g)",
            min_value=0,
            step=10
        )

    st.header("이동수단")

    transportation_labels = {
            info["label"]: key
            for key, info in transportation.items()
        }
    
    col1, col2, col3 = st.columns(3)
    with col1:
        selected = st.selectbox(
            "평소 이동수단",
            transportation.keys()
        )
        user_inputs["평소 이동수단"] = transportation_labels[selected]
    
    with col2:
        selected = st.selectbox(
            "오늘 이동수단",
            transportation.keys()
        )
        user_inputs["오늘 이동수단"] = transportation_labels[selected]

    with col3:
        user_inputs["이동거리"] = st.number_input(
            "이동거리(km)",
            min_value=0,
            step=1
        )
    return user_inputs

def calculate_electric(user_inputs):

    total = 0

    for key, info in electric.items():
        value = user_inputs[key]
        factor = info["factor"]

        total += value / 60 * factor * 0.4173 / 1000

    return total

def calculate_recycle(user_inputs):

    total = 0

    total += user_inputs["can"] * recycle["can"]["factor"] * 11 /1000000
    total += user_inputs["glass"] * recycle["glass"]["factor"] * 400 / 1000000
    total += user_inputs["plastic"] * recycle["plastic"]["factor"] * 15 / 1000000

    return total

def calculate_replacement(user_inputs):

    total = 0

    before = user_inputs["평소식단"]
    after = user_inputs["오늘식단"]
    total += (meal[after]["factor"] - meal[before]["factor"]) * user_inputs["섭취량"] / 1000

    before_t = user_inputs["평소 이동수단"]
    after_t = user_inputs["오늘 이동수단"]
    total += (transportation[after_t]["factor"] - transportation[before_t]["factor"]) * user_inputs["이동거리"] 

    return total

def calculate_total(user_inputs):

    electric = calculate_electric(user_inputs)
    meal = calculate_replacement(user_inputs)
    recycle = calculate_recycle(user_inputs)

    total = electric + meal - recycle

    return total

def show_result(total):

    st.success(f"총 탄소배출량 : {total*1000:.2f} kgCO₂")

user_inputs = {}

user_inputs.update(create_inputs())
user_inputs.update(create_replacement())

if st.button("탄소배출량 계산"):

    total = calculate_total(user_inputs)

    show_result(total)