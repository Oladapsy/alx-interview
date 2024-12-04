#!/usr/bin/python3
"""calculating perimeter of an island"""


def island_perimeter(grid):
    """return perimeter of island in grid"""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                perimeter += 4

                # Check above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                # Check below
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1
                # Check left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1
                # Check right
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
