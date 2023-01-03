#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        print("FizzBuzz", end=" ")
        continue
    elif a % 5 == 0:
        print("Buzz", end=" ")
        continue
    elif a % 3 == 0:
        print("Fizz", end=" ")
        continue
    print(a, end=" ")
