from all_functions import search_data, calculate_bmi, calculate_nutrition
import pandas as pd
import pytest

def test_calculate_bmi():
    bmi, calorie_intake = calculate_bmi(170, 50, 20,'F')
    assert bmi == 17.30
    assert calorie_intake ==1301.50

def test_calculate_bmi_Female():
    bmi, calorie_intake = calculate_bmi(170, 50, 20, 'F')
    assert bmi == 17.30
    assert calorie_intake == 1301.50

def test_calculate_bmi_Male():
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




