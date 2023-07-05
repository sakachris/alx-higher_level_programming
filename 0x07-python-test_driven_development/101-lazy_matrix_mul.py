#!/usr/bin/python3
"""

    Matrix multiplication module

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplying two matrices

    """
    return np.matmul(m_a, m_b)
