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
    print("Yayyyyy: You have guessed the correct number Congratulations.............. :-)")   
guess(15)


