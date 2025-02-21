import random


def task_1():
    number_list = []
    for num in range(50):
        random_number = random.randint(1, 200)
        number_list.append(random_number)

    highest_number = 0

    for num in number_list:
        if num > highest_number:
            highest_number = num

    print(number_list)
    print(highest_number)


def task_2():
    sum = 0
    for num in range(1, 101):
        sum += num
    print(sum)


def final_task():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = []

    for i in range(nr_letters):
        random_letters = random.randint(0, len(letters) - 1)
        password.append(letters[random_letters])
    for i in range(nr_symbols):
        random_symbols = random.randint(0, len(symbols) - 1)
        password.append(symbols[random_symbols])
    for i in range(nr_numbers):
        random_numbers = random.randint(0, len(numbers) - 1)
        password.append(numbers[random_numbers])

    password_final = ""

    for k in range(len(password)):
        random_placement = random.randint(0, len(password) - 1)
        password_final += password[random_placement]
        password.pop(random_placement)

    print(password_final)


def run():
    final_task()


if __name__ == "__main__":
    run()