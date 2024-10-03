import re


def search_data(df, keyword):
    # Make sure the column name is correct
    descs = df["food"]
    loc = []
    for item in descs:
        if re.search(keyword, item, re.IGNORECASE):
            loc.append(True)
        else:
            loc.append(False)
    return loc


def prepare_macro_nutrient_data(selected_food_data):
    macro_nutri_type = ["Fat", "Protein", "Carbo", "Sugars", "Fiber"]
    macro_nutri_value = [
        float(selected_food_data[2]),
        float(selected_food_data[8]),
        float(selected_food_data[6]),
        float(selected_food_data[7]),
        float(selected_food_data[9])
    ]
    return macro_nutri_type, macro_nutri_value


def prepare_micro_nutrient_data(selected_food_data):
    micronutrient_data = {
        "Cholesterol": float(selected_food_data[10]),
        "Sodium": float(selected_food_data[11]),
        "Vitamin A": float(selected_food_data[13]),
        "Vitamin C": float(selected_food_data[21]),
        "Calcium": float(selected_food_data[25]),
        "Iron": float(selected_food_data[27]),
        "Zinc": float(selected_food_data[33])
    }

    others_value = sum(value for value in micronutrient_data.values() if value <= 1)
    micro_nutri_value = [value for value in micronutrient_data.values() if value > 1]
    micro_nutri_type = [nutrient for nutrient, value in micronutrient_data.items() if value > 1]

    if others_value > 0:
        micro_nutri_type.append("Others")
        micro_nutri_value.append(others_value)

    return micro_nutri_type, micro_nutri_value
