import calc
import util
print("Добро пожаловать!")
a = 21
b = 44
menu = {
        1 : {
            "desc": "Результат сложения",
            "func": calc.sum
        },
        2 : {
            "desc": "Результат вычитания",
            "func": calc.sub
        },
        3 : {
            "desc": "Результат умножения",
            "func": calc.mult
        },
        4 : {
            "desc": "Результат деления",
            "func": calc.div
        },
        5 : {
            "desc": "Остаток от деления",
            "func": calc.ost
        }
    }

for i in menu:
    print(menu[i]["desc"] + ": " + str(menu[i]["func"](a, b)))



# for i in menu:
#     print(menu[i](a, b))

print(util.num_input(a, b))

ans1 = util.num_input(1, 4)

if ans1 == 1:
    f = calc.sum

elif ans1 == 2:
    f = calc.sub

elif ans1 == 3:
    f = calc.mult

elif ans1 == 4:
    f = calc.div

print(f(a, b))



# spisok = [11, 22, 33]
#
# tup = (5, 8,7,9)
# dict = {"John":120, "Maria":100, "olen":200}
# dict["John"] = 150
# dict["chingishan"] = 123
# print(dict.items())
#
# for t in dict.items():
#     print(f"{t[0]} - {t[1]}")
#
# print()
#
# for k, v in dict.items():
#     print(f"{k} - {v}")

print()

for k in dict:
    print(f"{k} - {dict[k]}")


