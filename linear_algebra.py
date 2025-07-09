import numpy as np


def add_matrices(a, b):
    return np.add(a, b)


def subtract_matrices(a, b):
    return np.subtract(a, b)


def dot_product(a, b):
    return np.dot(a, b)


def magnitude(a):
    return np.linalg.norm(a)


def transpose_matrix(a):
    return a.T
