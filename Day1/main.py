def task_1():
    print("Hello World")


def task_2():
    print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n"
          "2. Knead the dough for 10 minutes.\n"
          "3. Add 3g of Salt.\n"
          "4. Leave to rise for 2 hours.\n"
          "5. Bake at 200 degrees C for 30 minutes.")


def task_3():
    name = input("What is your name? ")
    print("Hello " + name + "!")


def task_4():
    #print(len(input("What is your name? ")))
    user_name = input("What is your name? ")
    name_length = len(user_name)
    print(name_length)


def final_task():
    print("Welcome to the Band Name Generator!")
    city = input("What city did you grow up in? ")
    pet_name = input("What is the name of your latest pet? ")
    print("Your band name is " + city + " " + pet_name + "!")


def run():
    final_task()


if __name__ == "__main__":
    run()

