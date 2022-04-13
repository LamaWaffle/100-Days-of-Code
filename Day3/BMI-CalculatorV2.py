height = float(input("Enter your height in m: \n"))
weight = float(input("Enter you weight in kg: \n"))

bmi = round(weight / height ** 2)
# bmi = 18

if bmi <= 18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal Weight")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are Overweight")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print(f"Your BMI is {bmi}, you are Clinically Obese, please get some help")
