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
#return df['Food'].str.contains(keyword, case=False, na=False)


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

    # Sort the macronutrient data in descending order for better visualisation
    for i in range(len(macro_nutri_value) - 1):
        for j in range(i + 1, len(macro_nutri_value)):
            if macro_nutri_value[i] > macro_nutri_value[j]:
                # Swap values
                macro_nutri_value[i], macro_nutri_value[j] = macro_nutri_value[j], macro_nutri_value[i]
                # Swap corresponding types
                macro_nutri_type[i], macro_nutri_type[j] = macro_nutri_type[j], macro_nutri_type[i]

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

    # Sort the macronutrient data in descending order for better visualisation
    for i in range(len(micro_nutri_value) - 1):
        for j in range(i + 1, len(micro_nutri_value)):
            if micro_nutri_value[i] > micro_nutri_value[j]:
                # Swap values
                micro_nutri_value[i], micro_nutri_value[j] = micro_nutri_value[j], micro_nutri_value[i]
                # Swap corresponding types
                micro_nutri_type[i], micro_nutri_type[j] = micro_nutri_type[j], micro_nutri_type[i]

    return micro_nutri_type, micro_nutri_value



def filter_nutrients(df, nutrient_name, nutrient_level, min_value_str, max_value_str):
    # Check if nutrient name is provided
    if nutrient_name in df.columns:  # Ensure nutrient name is valid
        # Check if both min and max values are provided
        if min_value_str and max_value_str:  # Both values are provided
            min_value = float(min_value_str)  # Convert to float
            max_value = float(max_value_str)  # Convert to float
            # Filter based on nutrient range
            nutrient = df[nutrient_name]
            range_filter = (nutrient >= min_value) & (nutrient <= max_value)
            df = df.loc[range_filter]
            return df
        # If min or max are not provided, filter by level
        elif nutrient_level:
            nutrient = df[nutrient_name]
            nutrient_max = df[nutrient_name].max()
            low_threshold = nutrient_max * 0.33
            mid_threshold = nutrient_max * 0.66

            if nutrient_level == 'Low':
                df = df[nutrient < low_threshold]
            elif nutrient_level == 'Mid':
                df = df[(nutrient >= low_threshold) & (nutrient <= mid_threshold)]
            elif nutrient_level == 'High':
                df = df[nutrient > mid_threshold]

            return df
def calculate_bmi(height,weight,age,gender):
    bmi = weight / (height * height)

    # Estimate daily calorie intake (simple calculation)
    if gender == 'M':
        calorie_intake = 10 * weight + 6.25 * (height * 100) - 5 * age + 5
    elif gender == 'F':
        calorie_intake = 10 * weight + 6.25 * (height * 100) - 5 * age - 161
    else:
        raise ValueError("Invalid gender input!")

    return round(bmi, 2), round(calorie_intake, 2)

def calculate_nutrition(carbs_per_100g,sugars_per_100g,fat_per_100g, protein_per_100g,fiber_per_100g,cal_per_100g, amount):
    carbs = (carbs_per_100g / 100) * amount
    sugars = (sugars_per_100g / 100) * amount
    protein = (protein_per_100g / 100) * amount
    fat = (fat_per_100g / 100) * amount
    fiber = (fiber_per_100g / 100) * amount
    cal = (cal_per_100g / 100) * amount

    return carbs, sugars, protein, fat, fiber, cal

