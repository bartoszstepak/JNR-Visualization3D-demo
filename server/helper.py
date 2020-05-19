from math import *
import numpy as np


def normalize_real_vector(vector):
    dim = len(vector)
    tmp_sum = 0

    for i in range(dim):
        tmp_sum = tmp_sum + pow(vector[i], 2)

    vector_length = sqrt(tmp_sum)
    normalized_vector = []

    if vector_length > 0:
        for i in range(dim):
            normalized_vector.append(vector[i] / vector_length)

    return np.asarray(normalized_vector)


def normalize_complex_vector(vector):
    vector_oo = vector - vector.real.min() - 1j * vector.imag.min()
    return vector_oo/np.abs(vector_oo).max()


def get_hermitian_operator(dimension=3):
    random_array = np.random.rand(dimension, dimension)
    matrix = np.asmatrix(random_array)

    conjugate_transposed_matrix = matrix.getH()
    matrices_sum = np.add(matrix, conjugate_transposed_matrix)
    matrices_sum_as_array = np.asarray(matrices_sum)
    divided_sum = matrices_sum_as_array / 2

    return divided_sum


def get_fibonacci_sphere_as_vectors(samples=1):
    points = []
    phi = pi * (3. - sqrt(5.))

    for i in range(samples):

        y = 1 - (i / float(samples - 1)) * 2
        theta = phi * i
        x = cos(theta) * 1
        z = sin(theta) * 1
        vector = (x, y, z)

        if len(vector) == 3:
            points.append(vector)

    return points
