#!/usr/bin/python3
"""

    Matrix multiplication module

"""


def matrix_mul(m_a, m_b):
    """
    Multiplying two matrices
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(isinstance(i, list) for i in m_a) is False:
        raise TypeError("m_a must be a list of lists")
    if any(isinstance(i, list) for i in m_b) is False:
        raise TypeError("m_b must be a list of lists")
    if all(isinstance(e, (int, float)) for rw in m_a for e in rw) is False:
        raise TypeError("m_a should contain only integers or floats")
    if all(isinstance(e, (int, float)) for rw in m_b for e in rw) is False:
        raise TypeError("m_b should contain only integers or floats")
    len_a = len(m_a[0]) if m_a else None
    len_b = len(m_b[0]) if m_b else None
    if all(len(m_row) == len_a for m_row in m_a) is False:
        raise TypeError("each row of m_a must be of the same size")
    if all(len(m_row) == len_b for m_row in m_b) is False:
        raise TypeError("each row of m_b must be of the same size")
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(r * c for r, c in zip(a_row, b_col)) for b_col in zip(*m_b)]
            for a_row in m_a]
