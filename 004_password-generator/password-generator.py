import random as rd 

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!#$%&/()='¿?"

print("You password must be between 1 and 99")

length = int(input("Length: "))

if length <= 0:
    print("I didn't know you could write without numbers.")
    
elif length >= 100:
    print("Slow down, darling, it's not a novel.")    
    
else:    
    use_numbers = input("Do you want to use numbers? (Yes/No): ").lower()
    use_symbols = input("Do you want to use symbols? (Yes/No): ").lower()

    available_characters = letters 

    if use_numbers == "yes": 
        available_characters += numbers

    if use_symbols == "yes":
        available_characters += symbols

    password = ""

    for i in range(length):
        password += rd.choice(available_characters)
        
    print(f"Generated password: {password}")