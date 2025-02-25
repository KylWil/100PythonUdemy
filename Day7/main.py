import random


def print_hangman(lives):
    print("___")
    if lives == 6:
        print(" |")
    elif lives == 5:
        print(" |\n"
              " O")
    elif lives == 4:
        print(" |\n"
              " O\n"
              " |")
    elif lives == 3:
        print(" |\n"
              " O\n"
              "/|")
    elif lives == 2:
        print(" |\n"
              " O\n"
              "/|\\")
    elif lives == 1:
        print(" |\n"
              " O\n"
              "/|\\\n"
              "/")
    else:
        print(" |\n"
              " O\n"
              "/|\\\n"
              "/ \\")


def run():
    lives = 6
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = word_list[random.randint(0, len(word_list) - 1)]
    player_guess_list = ["_"] * len(chosen_word)
    chosen_word_list = []

    for char in chosen_word:
        chosen_word_list.append(char)

    while 1 <= lives <= 6:
        print(f"Lives: {lives}")
        print_hangman(lives)
        print(" ".join(player_guess_list))
        player_letter_guess = input("Guess a letter!: ").lower()

        accumulator = 0
        deduction = 1
        for letter in chosen_word_list:
            if player_letter_guess == letter:
                player_guess_list[accumulator] = letter
                deduction = 0
            accumulator += 1

        if deduction == 1:
            lives -= 1

        if player_guess_list == chosen_word_list:
            lives = 999




    if lives == 0:
        print_hangman(0)
        print("Sorry, you lose!\n"
              f"The word was: {chosen_word}")
    else:
        print("Congrats, you win!\n"
              f"The word was: {chosen_word}")


if __name__ == "__main__":
    run()
