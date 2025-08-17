y = int(input("Введите год: "))


def is_year_leap(y):

    if y % 4 == 0:
        print(f"Год {y}: ", True)
    else:
        print(f"Год {y}: ", False)

    is_year_leap(y)
