#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: NOV 2022
# This program adds positive number using loops


def main():
    # This program adds positive number using loops
    loop_counter = 0
    add_int = 0

    # input,process,output
    input_as_string = input("How many positive integers do you want to add?: ")

    try:
        input_as_integer = int(input_as_string)
        if input_as_integer > 0:
            while loop_counter < input_as_integer:
                loop_counter = loop_counter + 1
                user_as_string = input("\nEnter a number to add: ")
                user_as_int = int(user_as_string)
                if user_as_int < 0:
                    continue
                add_int = add_int + user_as_int
                sum = add_int
            print("\nSum of all the positive numbers is = {0}".format(sum))
        else:
            print("\nPlease input a positive integer.")
    except ValueError:
        print("\nInvalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
