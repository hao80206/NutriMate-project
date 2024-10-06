# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/XXXX/XXXXX.git

---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions** | **Test Functions**                               |
|----------------------|--------------------------------------------------|
| `add(x1,x2)`         | `test_add_valid()` <br> `test_add_invalid`       |
| `divide(x1,x2)`      | `test_divide_valid()` <br> `test_divide_invalid` |
| `...`                | `...`                                            |

---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```
### Test Case 2:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 3:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 4:
- **Test Function/Module**
  - `test_divide_valid()`
  - `test_divide_invalid()`
- **Tested Function/Module**
  - `divide(a, b)`
- **Description**
  - A brief description of the tested function's usage, including its purpose, input, and output.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```


### Test Case 5:
- **Test Function/Module**
  - test_calculate_bmi_Female()
  - test_calculate_bmi_Male()`
  - test_calculate_bmi_invalid_input_gender()
  
- **Tested Function/Module**
  - `calculate_bmi(height,weight,age,gender)`
- **Description**
  - This function calculates the user's Body Mass Index (BMI) and their recommended daily calorie intake based on the user's height, weight, age, and gender.
  
**1) Valid Input and Expected Output**  

| **Valid Input** | **Expected Output**                       |
|----|-------------------------------------------|
| `calculate_bmi(1.7, 50, 20, 'F')` | `bmi == 17.30, calorie_intake == 1301.50` |
| `calculate_bmi(1.75, 65, 20,'M')` | `bmi == 21.22, calorie_intake == 1648.75`         |


- **1) Code for the Test Function**
```python
def test_calculate_bmi_Female():
    bmi, calorie_intake = calculate_bmi(1.7, 50, 20, 'F')
    assert bmi == 17.30
    assert calorie_intake == 1301.50

def test_calculate_bmi_Male():
    bmi, calorie_intake = calculate_bmi(1.75, 65, 20,'M')
    assert bmi == 21.22
    assert calorie_intake == 1648.75
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `calculate_bmi(1.70, 50, 20, 'X')`               | `Invalid gender input!`  |

- **2) Code for the Test Function**
```python
def test_calculate_bmi_invalid_input_gender():
    with pytest.raises(ValueError): 
        calculate_bmi(1.70, 50, 20, 'X')
```

### Test Case 6:
- **Test Function/Module**
  - test_calculate_nutrition()
  - test_calculate_nutrition_zero_amount()
  - test_calculate_nutrition_zero()
  - test_calculate_nutrition_negative_amount()
  
- **Tested Function/Module**
  - `calculate_nutrition(carbs_per_100g,sugars_per_100g,fat_per_100g, protein_per_100g,fiber_per_100g,cal_per_100g, amount):`
- **Description**
  - This function calculates the amount of macronutrients (carbohydrates, sugars, fats, protein, and fiber) and calories consumed based on the amount of food eaten. The nutrient values are provided per 100g, and the function scales these values according to the user-specified amount (in grams) of food. The function returns the calculated amounts for each nutrient and the corresponding caloric value.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                                                             | **Expected Output**                     |
|---------------------------------------------------------------------------------------------|-----------------------------------------|
| `calculate_nutrition(30, 15, 20, 10, 5, 100, 200)` | `carbs == 60, sugars == 30, protein == 20, fat == 40, fiber == 10, cal == 200` |
| `calculate_nutrition(50, 20, 30, 10, 5, 200, 0)`  | `carbs == 0, sugars == 0, protein == 0, fat == 0, fiber == 0, cal == 0`          |
| `calculate_nutrition(0, 0, 0, 0, 0, 0, 100)`      | `carbs == 0, sugars == 0, protein == 0, fat == 0, fiber == 0, cal == 0`          |


- **1) Code for the Test Function**
```python
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

def test_calculate_nutrition_negative_amount():
    with pytest.raises(ValueError): 
        calculate_nutrition(0, 0, 0, 0, 0, 0, '-100')
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `calculate_nutrition(0, 0, 0, 0, 0, 0, '-100')`               | `Please enter a valid numeric value for amount.`  |

- **2) Code for the Test Function**
```python
def test_calculate_nutrition_negative_amount():
    with pytest.raises(ValueError): 
        calculate_nutrition(0, 0, 0, 0, 0, 0, '-100')

```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
