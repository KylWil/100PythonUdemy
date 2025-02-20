import random


def task_1():
    flip = random.randint(0,1)

    if flip == 0:
        print("Heads")

    else:
        print("Tails")


def task_2():
    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
    random_friend = random.randint(1, len(friends))
    print(friends[random_friend - 1])


def final_task():
    choices = ["Rock", "Paper", "Scissors"]
    player_choice = input("Rock, Paper, or Scissors? ")
    computer_choice = choices[random.randint(0, 2)]

    if computer_choice == "Rock":
        print("Computer chose: Rock")
        if player_choice == "Rock":
            print("We tie")
        elif player_choice == "Paper":
            print("You win")
        else:
            print("You lose")
    elif computer_choice == "Paper":
        print("Computer chose: Paper")
        if player_choice == "Rock":
            print("You lose")
        elif player_choice == "Paper":
            print("We tie")
        else:
            print("You win")
    else:
        print("Computer chose: Scissors")
        if player_choice == "Rock":
            print("You win")
        elif player_choice == "Paper":
            print("You lose")
        else:
            print("We tie")



def run():
    final_task()


if __name__ == "__main__":
    run()