from random import randint


def generate_number():
    randomNumber = randint(0, 10)
    return randomNumber


def main():
    theNumber = generate_number()
    attempts = 0

    while True:
        print("Guess the number (between 0 and 10):")
        number = input("Enter your guess: ")

        try:
            number = int(number)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if number == theNumber:
            print(
                "Congratulations! You guessed the correct number {} in {} attempts.".format(
                    theNumber, attempts
                )
            )
            break
        elif number > theNumber:
            print("Go Lower")
        elif number < theNumber:
            print("Go Higher")

        print("=============================")


main()
