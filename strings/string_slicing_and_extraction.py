#Substring slicing and Extraction

email = input("Please enter your email: ")
print('your email is: ' + email)
point = email.find('@')
username = email[0:point]
print('your username is: ' + username)
domain = email[point+1:]
print('your domain is: '+domain)
print(f'first character: {email[0]} and last character: {email[-1]}')
