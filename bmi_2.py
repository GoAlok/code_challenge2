"""
    - Under 18.5 = underweight
    - Over 18.5 but below 25 = normal weight
    - over 25 but below 30 = over weight
    - over 30 but below 35 = obese
    - above 35 = clinically obese
"""

print('---- BMI CALCULATOR ----')

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / height ** 2) 
# bmi_as_int = int(bmi)
# print(bmi_as_int)

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, and you are Underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, and you are Normal Weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, and you are Overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, and you are Obese.")
else:
    print(f"Your BMI is {bmi}, and you are Clinically Obese.")

