'''18. BMI Calculator
- Develop a program to calculate BMI:
- Input: Weight (kg) and height (m).
- Output: BMI value and corresponding category (Underweight, Normal, Overweight,
Obese).'''


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)     # BMI formula: weight (kg) / height**2 (m)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI, CATEGORY = calculate_bmi(weight, height)

print(f"Your BMI is: {round(BMI,3)}")
print(f"Category: {CATEGORY}")
