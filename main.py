import calc
import util

a = 21
b = 44
print(util.num_input(a, b))

ans1 = util.num_input(1, 4)

if ans1 == 1:
    print(calc.sum(a, b))

elif ans1 == 2:
    print(calc.sub(a, b))

elif ans1 == 3:
    print(calc.mult(a,b))

elif ans1 == 4:
    print(calc.div(a,b))