#!/usr/bin/python3
"""
Pascal's Triangle module.
This module provides a function to generate Pascal's triangle.
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    
    Args:
        n (int): The number of rows of the triangle to generate.

    Returns:
        List[List[int]]: A list of lists, where each sublist represents a row in Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)
    
    return triangle
