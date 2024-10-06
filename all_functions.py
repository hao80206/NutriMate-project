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

