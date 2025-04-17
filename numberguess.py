import random
number = random.randint(1,100)
attempts=0
print("Welcome to number guesssig game ")
attempts += 1
while guess != number:
    guess=int(input('Guess a number between 1 to 100: '))
    attempts+=1
    if guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
    else:
        print(f"You guessedit in {attempts} attempts")
