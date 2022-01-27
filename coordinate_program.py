#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan 25, 2022
# This program asks the user for two points and displays the midpoint,
# distance and line equation of the two points

import math


def midpoint(x1, y1, x2, y2):
    # calculate the midpoint of two points
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    # display the midpoint as a coordinate
    midpoint = "({:.2f}, {:.2f})". format(midpoint_x, midpoint_y)
    return midpoint


def distance(x1, y1, x2, y2):
    # calculate the distance of two points
    distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
    return distance


def equation_line(x1, y1, x2, y2):
    # calculate the equation of the line for the two points
    m_value = ((y2-y1) / (x2-x1))
    b_value = (y1 - (x1 * m_value))

    # display the line equation in the form of y=mx+b
    line_equation = "y = {:.2f}x + {:.2f}". format(m_value, b_value)
    return line_equation


def main():
    # Display opening message to the user
    print("This program calculates the midpoint, distance"
          "and equation of the line given two points!!")
    print()
    while True:
        # get the x-coordinate of the first point
        user_x1_string = input("Enter the x-coordinate of the first point: ")
        try:
            # check that it is a number
            user_x1_float = float(user_x1_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a valid input. Try again."
                  . format(user_x1_string))

    while True:
        # get the y-coordinate of the first point
        user_y1_string = input("Enter the y-coordinate of the first point: ")
        try:
            # check that it is a number
            user_y1_float = float(user_y1_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a valid input. Try again."
                  . format(user_y1_string))
    print()

    while True:
        # get the x-coordinate of the second point
        user_x2_string = input("Enter the x-coordinate of the second point: ")
        try:
            # check that it is a number
            user_x2_float = float(user_x2_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a valid input. Try again."
                  . format(user_x2_string))

    while True:
        # get the y-coordinate of the second point
        user_y2_string = input("Enter the y-coordinate of the second point: ")
        try:
            # check that it is a number
            user_y2_float = float(user_y2_string)
            break
        except ValueError:
            # error message if the input is not a number
            print("{} is not a number, try again.". format(user_y2_string))
    print()

    # call functions to calculate the midpoint, distance and line equation
    midpoint_result = midpoint(user_x1_float, user_y1_float,
                               user_x2_float, user_y2_float)
    distance_result = distance(user_x1_float, user_y1_float,
                               user_x2_float, user_y2_float)
    equation_line_result = equation_line(user_x1_float, user_y1_float,
                                         user_x2_float, user_y2_float)

    # display the midpoint, distance and line equation
    print("The midpoint of the two points is: {}". format(midpoint_result))
    print()
    print("The distance between the two points is: {:.2f}"
          . format(distance_result))
    print()
    print("The equation of the line for the two points is: {}"
          . format(equation_line_result))


if __name__ == "__main__":
    main()
