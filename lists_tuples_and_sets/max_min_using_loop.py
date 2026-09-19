# Max Min without using built ins

numbers = list(map(float, input("Enter as many numbers as you like: ").split()))
largest = smallest = numbers[0]
for n in range(1, len(numbers)):
    if largest < numbers[n]:
        largest = numbers[n]
    elif smallest > numbers[n]:
        smallest = numbers[n]

print(f'MAX value is {largest}, and the MIN value is {smallest}')