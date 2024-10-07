#!/usr/bin/python3
"""
This module contains a function that generates Pascal's Triangle.

The pascal_triangle function returns a list of lists, where each sublist
represents a row of Pascal's Triangle up to n rows.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.
    Pascal's Triangle is a triangular array of numbers where each number is the
    sum of the two numbers directly above it in the previous row.
    :param n: Number of rows to generate
    :type n: int
    :return: A list of lists representing Pascal's Triangle
    :rtype: list of lists of int
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    # Initialize the triangle with the first row
    triangle = [[1]]  # The first row is always [1]
    # Generate subsequent rows of Pascal's Triangle
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Each element in the row (except for the first and last) is the sum of
        # the two elements directly above it from the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with a 1
        row.append(1)
        # Append the generated row to the triangle
        triangle.append(row)
    return triangle
