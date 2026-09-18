#Practice Question 1
first_name = 'Siddhant'
last_name = 'Sinha'
#full_name = first_name + ' ' + last_name
#full_name = '{} {}'.format(first_name,last_name)
full_name = f'{first_name} {last_name}'
print(f'Hello, {full_name.upper()}')
print(f'The total character count of your name is: {len(full_name)}')