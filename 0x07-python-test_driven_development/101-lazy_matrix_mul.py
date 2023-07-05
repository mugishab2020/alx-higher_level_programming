#!/usr/bin/python3
""" use numpy to multiply two matrices the lazy way"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    return np.matmul(m_a, m_b)
