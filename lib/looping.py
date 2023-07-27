#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count_num = 10
    while count_num > 0:
        print(count_num)
        count_num -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    square_list = [num * num for num in int_list]
    return square_list

def fizzbuzz():
    # code goes here!
    
    for num in range(1, 101):
        if (int(num) % 15) == 0:
            print("FizzBuzz")
        elif (int(num) % 3) == 0:
            print("Fizz")
        elif (int(num) % 5) == 0:
            print("Buzz")
        else:
            print(num)