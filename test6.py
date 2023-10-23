import random

var = random.randint(1,100)

print(var)

if var % 15 == 0:
    print("FizzBuzz")
elif var % 5 == 0:
    print("Buzz")
elif var % 3 == 0:
    print("Fizz")
else:
    print(var)

               