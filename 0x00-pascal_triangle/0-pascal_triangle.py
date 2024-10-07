#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.
    :param n: Number of rows to generate
    :return: List of lists representing Pascal's Triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's Triangle

    # Generate each row of Pascal's Triangle
    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Each element in the row is the sum of the two elements above it
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle

