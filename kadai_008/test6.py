# 条件分岐のif文で処理を切り替えよう
import random

var = random.randint(1,100)

print(var)

if var % 3 == 0:
    print(var,"Fizz")
elif var % 5 == 0:
    print(var,"Buzz")
if var % 15 == 0:
    print(var,"FizzBUzz")
else:
    print(var)

               
