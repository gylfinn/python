weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_int = float(weight_str)
height_int = float(height_str)
height_int = height_int / 100

bmi = (weight_int/(height_int ** 2))

print("BMI is: ", bmi) # do not change this line
