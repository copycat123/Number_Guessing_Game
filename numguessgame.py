
import random
import sys

print('------------------------------------\n'
      'WELCOME TO OUR NUMBER GUESSING GAME \n')


def start_game():
    # make a random number
    number = random.randint(1, 10)

    guess_game = 0

    while True:
        # show how many guesses there is left
        print("You have {}/7 guesses \n".format(guess_game))

        # ask the user for a number from 1 to a 10
        try:
            guess = (input("Guess the number between 1 to 10: "))

            # if the user wants to quit, then quit the program
            if guess == "":
                print("Bye!")
                break
            guess = int(guess)
        except ValueError:
            print('This is not a number \n')
            continue

        # tell the user if they need to guess higher or lower
        if guess > number:
            if not guess_game > 6:
                print('The number is too high try lower')

        elif guess < number:
            if not guess_game > 6:
                print('The number is too low try higher')

        # if the user got the number, tell the user that they won
        elif guess == number:
            print('You got the number! You win! The number was {}'.format(number))
            play_again = (
                input('Want to play! Enter yes/no or simply press "ENTER" to exit ').lower())
            if play_again == "yes":
                print("Here we go again \n")
                start_game()
            elif play_again == "no":
                print('Game Over')
                sys.exit()
            else:
                break

        # if the user guessed more than six times, tell them that they lost
        if guess_game > 6:
            print('Too bad but good effort! The number was {}'.format(number))
            play_again = (
                input('Want to play! Enter yes/no or simply press "ENTER" to exit ').lower())
            if play_again == "y":
                print("Here we go again \n")
                start_game()
            elif play_again == "n":
                print('Game Over')
                sys.exit()
            else:
                break
        guess_game += 1
        print('\n')


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
