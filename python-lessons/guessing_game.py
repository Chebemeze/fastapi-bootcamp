SECRET_NUMBER  = 7

while True:
    guessed_number = int(input("Guess the number: "))
    if guessed_number == SECRET_NUMBER:
        print("Correct! You guessed the number.")
        break
    elif guessed_number > SECRET_NUMBER:
        print("Too high!")
    elif guessed_number < SECRET_NUMBER:
        print("Too low!")
