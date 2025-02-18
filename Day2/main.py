def task_1():
    word = "Hello"
    print("Hello"[len(word) - 1])


def task_2():
    print(len("12345"))


def task_3():
    print(type(123))
    print(type("Hello"))
    print(type(False))
    print(type(123.39))



def task_4():
    print("Number of letters in your name: " + str(len(input("Enter your name"))))


def final_task():
    print("Welcome to the tip calculator!")
    bill_total = float(input("What was the total bill? "))
    tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
    total_split = float(input("How many people to split the bill?"))
    per_person = round((bill_total/total_split) * (tip_percent/100 + 1), 2)

    print(f"Each person should pay: ${per_person}")





def run():
    final_task()


if __name__ == "__main__":
    run()
