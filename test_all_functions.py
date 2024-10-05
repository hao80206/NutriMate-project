from all_functions import prepare_micro_nutrient_data, prepare_macro_nutrient_data


def test_get_micro_pos():
    selected_food_data = [
        "cream cheese", 51.0, 5.0, 2.9, 1.3, 0.2, 0.8, 0.5, 0.9, 0.0,
        14.6, 0.016, 7.6, 0.2, 0.033, 0.064, 0.092, 0.097, 0.084,
        0.052, 0.096, 0.004, 0.0, 0.1, 0.008, 14.1, 0.082, 0.027,
        1.3, 0.091, 15.5, 19.1, 0.039, 7.07
    ]

    # Convert Sodium from g into mg
    converted_sodium = selected_food_data[11] * 100  # Index 11 is Sodium

    micronutrient_values = [
        selected_food_data[10],  # Cholesterol
        converted_sodium,
        selected_food_data[13],  # Vitamin A
        selected_food_data[21],  # Vitamin C
        selected_food_data[25],  # Calcium
        selected_food_data[27],  # Iron
        selected_food_data[33]  # Zinc
    ]

    others_sum = sum(value for value in micronutrient_values if value <= 10)  # Sum values <= 10
    expected_micro_type = ["Cholesterol", "Calcium", "Others"]
    expected_micro_values = [14.6, 14.1, others_sum]

    micro_nutri_type, micro_nutri_value = prepare_micro_nutrient_data(selected_food_data)
    assert micro_nutri_type == expected_micro_type
    assert micro_nutri_value == expected_micro_values


def test_get_macro_pos():
    selected_food_data = [
        "cream cheese", 51.0, 5.0, 2.9, 1.3, 0.2, 0.8, 0.5, 0.9, 0.0,
        14.6, 0.016, 7.6, 0.2, 0.033, 0.064, 0.092, 0.097, 0.084,
        0.052, 0.096, 0.004, 0.0, 0.1, 0.008, 14.1, 0.082, 0.027,
        1.3, 0.091, 15.5, 19.1, 0.039, 7.07
    ]

    expected_macro_type = ["Fat", "Protein", "Carbo", "Sugars", "Fiber"]
    expected_macro_value = [5.0, 0.9, 0.8, 0.5, 0.0]

    macro_nutri_type, macro_nutri_value = prepare_macro_nutrient_data(selected_food_data)
    assert macro_nutri_type == expected_macro_type
    assert macro_nutri_value == expected_macro_value
