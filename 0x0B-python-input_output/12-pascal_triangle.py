#!/usr/bin/python3
"""Module for pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n: Height of triangle.

    Returns:
        List of lists of integers.
    """

    if n <= 0:
        return []
    p_triangle = [[1]]
    while len(p_triangle) < n:
        first_list_el = [1]
        last_list_el = p_triangle[-1]
        for i in range(len(last_list_el) - 1):
            first_list_el.append(last_list_el[i] + last_list_el[i + 1])
        first_list_el.append(1)
        p_triangle.append(first_list_el)
    return p_triangle
