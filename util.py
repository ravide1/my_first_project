def fact(x):
    r = 1
    for i in range(1, x + 1):
        r = r * i
    return r


def num_input(min, max):
    ans = input(f"Введите число от {min} до {max} : ")
    while not ans.isdigit() or not min <= int(ans) <= max:
        print("Неверный ввод")
        ans = input(f"Введите число от {min} до {max} : ")
    return int(ans)