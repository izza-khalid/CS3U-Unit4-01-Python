#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: Oct 2019
# This program uses a while loop


def main():
    # this function uses a while loop
    counter = 0
    answer = 0
    
    # input
    number = int(input("Enter a positive integer: "))
    print("")

    # process & output
    while counter <= number:
        answer = counter + answer
        counter = counter + 1
    print("The sum is {0}".format(answer))
   

if __name__ == "__main__":
    main()
