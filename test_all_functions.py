from all_functions import prepare_micro_nutrient_data, prepare_macro_nutrient_data
import pandas as pd

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
