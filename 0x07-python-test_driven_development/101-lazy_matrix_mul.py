#!/usr/bin/python3
"""Module for lazy_matrix_mul function."""


def lazy_matrix_mul(m_a, m_b):
    """A function that multiplies 2 matrices by using module NumPy.

    Args:
        m_a: First matrix.
        m_b: Second matrix.

    Return:
        Product of two matrices.
    """

    return numpy.matmul(m_a, m_b)
