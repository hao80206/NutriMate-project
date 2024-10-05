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


def prepare_macro_nutrient_data(df, selected_food_data):
    columns = df.columns

    # Find the indices for the micronutrients, which start from "Cholesterol" to "Zinc"
    start_index = columns.get_loc("Fat")
    end_index = columns.get_loc("Water")

    macronutrient_data = {}  # Initialize an empty dictionary

    # Loop over the range from start_index to end_index (inclusive)
    for i in range(start_index, end_index + 1):
        if columns[i] not in ["Sodium", "Cholesterol"]:
            key = columns[i]  # Get the column name (key)
            value = float(selected_food_data[i])  # Get the value and convert it to float
            macronutrient_data[key] = value  # Add the key-value pair to the dictionary

    macro_nutri_value = []
    macro_nutri_type = []

    for nutrient, value in macronutrient_data.items():
        macro_nutri_type.append(nutrient)
        macro_nutri_value.append(value)

    return macro_nutri_type, macro_nutri_value


def prepare_micro_nutrient_data(df, selected_food_data):

    columns = df.columns

    # Find the indices for the micronutrients, which start from "Cholesterol" to "Zinc"
    start_index = columns.get_loc("Cholesterol")
    end_index = columns.get_loc("Zinc")

    micronutrient_data = {}  # Initialize an empty dictionary

    # Loop over the range from start_index to end_index (inclusive)
    for i in range(start_index, end_index + 1):
        if columns[i] not in ["Water", "Cholesterol"]:
            key = columns[i]  # Get the column name (key)
            value = float(selected_food_data[i])  # Get the value and convert it to float
            micronutrient_data[key] = value  # Add the key-value pair to the dictionary

    # Convert Sodium from grams to milligrams
    if "Sodium" in micronutrient_data:
        micronutrient_data["Sodium"] *= 1000

    """ If value less than 10mg then append to "Others" """
    others_value = 0
    micro_nutri_value = []
    micro_nutri_type = []

    for nutrient, value in micronutrient_data.items():
        if value <= 10:  # less than 10mg
            others_value += value
        else:
            micro_nutri_type.append(nutrient)
            micro_nutri_value.append(value)

    if others_value > 0:
        micro_nutri_type.append("Others")
        micro_nutri_value.append(others_value)

    return micro_nutri_type, micro_nutri_value
