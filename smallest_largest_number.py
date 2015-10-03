#!/usr/bin/env python

import argparse
import sys


def get_options():
    parser = argparse.ArgumentParser(prog='smallest_largest_number.py',
                                     description=("Program to return" +
                                                  " the smallest and" +
                                                  " largest number from" +
                                                  " a list of numbers."))
    parser.add_argument('--built-in', action='store_true',
                        help=("Use built-in python sorted() or " +
                              "custom sort function; default " +
                              "behavior is custom sort function"))
    parser.add_argument('number', nargs='+',
                        type=float,
                        help="List of numbers")
    options = parser.parse_args()
    return options


def sort_em(list):
    """
    Function to find the smallest and largest values
    from an unsorted list of numbers.

    Function implements selection sort.  This sorting algorithm was chosen
    because of two factors:
    - storage efficiency
    - stable (i.e. any elements that are equal retain their initial relative
      ordering)
    """
    for position in range(len(list)-1, 0, -1):
        largest_seat = 0
        for seat in range(1, position+1):
            if list[seat] > list[largest_seat]:
                largest_seat = seat

        interim = list[position]
        list[position] = list[largest_seat]
        list[largest_seat] = interim

if __name__ == "__main__":
    options = get_options()
    if options.built_in:
        print "Smallest numeric value: " + str(sorted(options.number)[0])
        print "Largest numeric value: " + str(sorted(options.number)[-1])
    else:
        sort_em(options.number)
        print "Smallest numeric value: " + str(options.number[0])
        print "Largest numeric value: " + str(options.number[-1])
    sys.exit()
