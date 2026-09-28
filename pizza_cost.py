#!/usr/bin/env python3
# Created By: elohim
# Date: sep 28, 2026
# This program  asks the user for the diameter of the
# pizza, it then calculates and displays the total cost
# of the pizza with tax .
LABOUR_COST = 0.75
RENTAL_COST = 1.00
INGRED_COST = 0.50
HST = 0.13


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = LABOUR_COST + RENTAL_COST + INGRED_COST * diameter
    tax = HST * subtotal
    total = subtotal + tax

    # output
    print(" ")
    print("The total cost is = ${:.2f}".format(total))


if __name__ == "__main__":
    main()
