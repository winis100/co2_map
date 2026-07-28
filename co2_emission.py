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

rooms = {
    "거실": living_room,
    "주방": kitchen,
    "다용도실": laundry_room,
    "재활용": recycle,
    "식사": meal
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

def calculate_electric(user_inputs):

    total = 0

    for key, info in electric.items():
        value = user_inputs[key]
        factor = info["factor"]

        total += value / 60 * factor * 0.4173 / 1000

    return total

def calculate_meal(user_inputs):

    total = 0

    return total

def calculate_recycle(user_inputs):

    total = 0

    total += user_inputs["can"] * recycle["can"]["factor"] * 11 /1000000
    total += user_inputs["glass"] * recycle["glass"]["factor"] * 400 / 1000000
    total += user_inputs["plastic"] * recycle["plastic"]["factor"] * 15 / 1000000

    return total

def calculate_total(user_inputs):

    electric = calculate_electric(user_inputs)
    meal = calculate_meal(user_inputs)
    recycle = calculate_recycle(user_inputs)

    total = electric + meal - recycle

    return total

def show_result(total):

    st.success(f"총 탄소배출량 : {total*1000:.2f} kgCO₂")

user_inputs = create_inputs()

if st.button("탄소배출량 계산"):

    total = calculate_total(user_inputs)

    show_result(total)