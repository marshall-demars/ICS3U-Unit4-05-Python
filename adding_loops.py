#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Nov 2022
# This program does addition using loops


def main():
    # This program does addition using loops

    counter = 0
    total_of_numbers = 0

    # Input, Process and Output
    added_as_string = input("How many positive whole numbers would you like to add: ")

    try:
        added_as_int = int(added_as_string)

        for counter in range(added_as_int):
            input_as_string = input("\nEnter a positive integer to add: ")
            number_as_int = int(input_as_string)
            if number_as_int < 0:
                continue
            elif number_as_int > 0:
                total = total + number_as_int
            else:
                break

        if number_as_int > 0 or number_as_int < 0:
            print("\nSum of all positive integers is {0}.".format(total_of_numbers))
    except Exception:
        print("\nInvalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
