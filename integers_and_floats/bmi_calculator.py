# BMI Calcutaor

weight, height = map(float, input('Please enter your weight in kg and height in m: ').split())
bmi = weight/(height**2)
print(f'Your BMI is: {bmi:.1f}')