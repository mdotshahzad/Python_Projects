# This Project will have randdom num between 1 to 15. You need to guess the correct number that 
# Computer choose.


import random
def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f"Guess the number between 1 and {x}: "))

        print(guess)
        if (guess < random_num):
            print("Your number is shorter than computer's number. try high")
        elif (guess > random_num):
            print("Your number is greater than computer's number try low")
    print(f"Yayyyyy: You have guessed the correct number {random_num}. Congratulations.............. :-)")   

def computer_guess(x):
    lower_bound = 1
    upper_bound = x

    feedback = ''

    while feedback != 'c':
        guess = random.randint(lower_bound, upper_bound)
        feedback = input(f"Is {guess} too Low (L), too high (H), or correct (C)").lower()

        if feedback == 'h':
            upper_bound = guess -1
            print("Your Number is high, try Low")
        elif feedback == 'l':
            lower_bound = guess +1
            print("Your Number is Low, try High")
    
    print(f"Yayyyy. Your Number {guess} is correct. Congrats")




print("Please select You want guess the Number or Computer will guess the Number.")
mode = input("Me | Computer:  ").lower()

if mode == "me":
    guess(15)
elif mode == "computer":
    computer_guess(15)


