#Program to calculate Simple Interest

principal, rate, time = map(float, input("Please Input Principal, Rate, Time : ").split())
simple_interest = (principal*rate*time)/100 
print(f'The Simple Interest on your {principal} for time {time} at rate {rate} is : {simple_interest:.2f}') # since im not using si for futher calculations here using round is redundant since :.2f does the same thing here