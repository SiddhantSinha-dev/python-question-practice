# List sum and average

num = []
while len(num) != 5:
    num = list(map(float, input("Please enter five numbers: ").split()))
total = sum(num)
avg = total/len(num)
print(f'The sum of numbers is {total} and the average is {avg}')

''' When you don't want to store variables for sum and avg 
print(f'sum of numbers is {sum(num)} and the avg is {sum(num)/len(num)}') '''

'''Without using sum() function
total = 0
c = 0

for n in num:
    total = total + n
    c+= 1
    
print(f'sum of numbers is {total} and the avg is {total/c}')'''