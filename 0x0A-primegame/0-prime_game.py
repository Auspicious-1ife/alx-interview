#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of lists representing the island grid,
                                    where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0
    
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell starts with 4 sides
                perimeter += 4
                
                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                
                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    
    return perimeter

