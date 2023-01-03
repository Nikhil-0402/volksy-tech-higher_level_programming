#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        print("FIZZBUZZ", end=" ")
        continue
    elif a % 5 == 0:
        print("BUZZ", end=" ")
        continue
    elif a % 3 == 0:
        print("FIZZ", end=" ")
        continue
    print(a, end=" ")
