password=input("enter the password:")
length_criteria = len(password) >= 8
uppercase_criteria = any(char.isupper() for char in password)
lowercase_criteria = any(char.islower() for char in password)
number_criteria = any(char.isdigit() for char in password)
special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password)

    
if all([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria]):
    print("Strong password")
else:
    print("Week Password")