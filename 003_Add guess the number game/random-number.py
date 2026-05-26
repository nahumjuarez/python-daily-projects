import random as rd

secret_number = rd.randint(1,100)
attemps = 0

while True:
    guess = int(input("¿Can you guess the number I'm thinking of? Try it... "))
    attemps += 1
    
    if guess < secret_number: 
        print("Mmmmmm... to low")
    elif guess > secret_number:
        print("It's a little bit high")
    else:
        print(f"WOOOOOW, It's correct. You made it at {attemps} attempts.")
        break