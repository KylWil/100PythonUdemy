def task_1():
    total = 0
    size = input("What size of pizza would you like, S M or L? ")
    pepperoni = input("Would you like pepperoni, Y or N? ")
    cheese = input ("How about extra cheese, Y or N? ")

    if size == "S":
        total += 15
        if pepperoni == "Y":
            total += 2
    elif size == "M":
        total += 20
        if pepperoni == "Y":
            total += 3
    else:
        total += 25
        if pepperoni == "Y":
            total += 3
    if cheese == "Y":
        total += 1

    print(f"Your final bill is ${total}.")


def final_task():
    print("Welcome to Treasure Island.\n"
          "Your mission is to find the treasure.")

    left_right = input("Left or Right? ")

    if left_right == "Left":
        swim_wait = input("Swim or Wait? ")

        if swim_wait == "Wait":
            which_door = input("Which door? ")

            if which_door == "Blue":
                print("Eaten by beasts. Game Over.")

            elif which_door == "Yellow":
                print("You Win!")

            elif which_door == "Red":
                print("Burned by fire. Game Over.")

            else:
                print("Game Over.")
        else:
            print("Attacked by trout. Game Over.")
    else:
        print("Fall into a hole. Game Over.")











def run():
    final_task()


if __name__ == "__main__":
    run()