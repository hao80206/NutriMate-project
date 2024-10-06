from all_functions import (search_data, calculate_bmi, calculate_nutrition,
                           prepare_micro_nutrient_data, prepare_macro_nutrient_data)
import pandas as pd
import pytest

# Load the DataFrame from CSV
df = pd.read_csv(r".\Food_Nutrition_Dataset.csv")

# Use the columns from the DataFrame directly
columns = list(df.columns)


def test_get_micro_pos():
    selected_food_data = df.iloc[0].tolist()  # Cream Cheese

    # Hardcode the expected micronutrient types and values based on sorted results
    expected_micro_type = ['Others', 'Copper', 'Potassium', 'Sodium', 'Selenium']
    expected_micro_values = [2.369, 14.1, 15.5, 16.0, 19.1]  # Sodium converted to mg and sum of "Others" values

    # Get the actual results from the function
    micro_nutri_type, micro_nutri_value = prepare_micro_nutrient_data(df, selected_food_data)

    # Assert the types and values
    assert micro_nutri_type == expected_micro_type, "Micronutrient type did not match expected sorted results"
    assert micro_nutri_value == expected_micro_values, "Micronutrient value did not match expected sorted results"


def test_get_macro_pos():
    selected_food_data = df.iloc[0].tolist()  # Cream Cheese

    expected_macro_type = ['Dietary Fiber',
                           'Polyunsaturated Fats',
                           'Sugars',
                           'Carbohydrates',
                           'Protein',
                           'Monounsaturated Fats',
                           'Saturated Fats',
                           'Fat',
                           'Water']
    expected_macro_value = [0.0, 0.2, 0.5, 0.8, 0.9, 1.3, 2.9, 5.0, 7.6]

    macro_nutri_type, macro_nutri_value = prepare_macro_nutrient_data(df, selected_food_data)
    assert macro_nutri_type == expected_macro_type, "Macronutrient type did not match expected sorted results"
    assert macro_nutri_value == expected_macro_value, "Macronutrient value did not match expected sorted results"

def test_calculate_bmi():
    bmi, calorie_intake = calculate_bmi(1.7, 50, 20,'F')
    assert bmi == 17.30
    assert calorie_intake ==1301.50

def test_calculate_bmi_Female():
    bmi, calorie_intake = calculate_bmi(1.7, 50, 20, 'F')
    assert bmi == 17.30
    assert calorie_intake == 1301.50

def test_calculate_bmi_Male():
    bmi, calorie_intake = calculate_bmi(1.75, 65, 20,'M')
    bmi, calorie_intake = calculate_bmi(175, 65, 20,'M')
    assert bmi == 21.22
    assert calorie_intake == 1648.75

def test_calculate_bmi_invalid_input_gender():
    with pytest.raises(ValueError):  # Assuming a ValueError is raised for invalid gender
        calculate_bmi(1.70, 50, 20, 'X')

def test_calculate_nutrition():
    carbs, sugars, protein, fat, fiber, cal = calculate_nutrition(30, 15, 20, 10, 5, 100, 200)
    assert carbs == 60  # (30 / 100) * 200
    assert sugars == 30  # (15 / 100) * 200
    assert protein == 20  # (10 / 100) * 200
    assert fat == 40  # (20 / 100) * 200
    assert fiber == 10  # (5 / 100) * 200
    assert cal == 200  # (100 / 100) * 200

def test_calculate_nutrition_zero_amount():
    carbs, sugars, protein, fat, fiber, cal = calculate_nutrition(50, 20, 30, 10, 5, 200, 0)
    assert carbs == 0
    assert sugars == 0
    assert protein == 0
    assert fat == 0
    assert fiber == 0
    assert cal == 0

def test_calculate_nutrition_zero():
    carbs, sugars, protein, fat, fiber, cal = calculate_nutrition(0, 0, 0, 0, 0, 0, 100)
    assert carbs == 0
    assert sugars == 0
    assert protein == 0
    assert fat == 0
    assert fiber == 0
    assert cal == 0




