from math import *
import numpy as np


def normalize_3d_vector(vector):

    if len(vector) == 3:
        x = vector[0]
        y = vector[1]
        z = vector[2]

        vector_length = sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

        if vector_length != 0:
            normalized_vector = x / vector_length, y / vector_length, z / vector_length

            return normalized_vector


def get_hermitian_operator(dimension=3):

    random_array = np.random.rand(dimension, dimension)
    matrix = np.asmatrix(random_array)

    conjugate_transposed_matrix = matrix.getH()
    matrices_sum = np.add(matrix, conjugate_transposed_matrix)
    matrices_sum_as_array = np.asarray(matrices_sum)
    divided_sum = matrices_sum_as_array/2

    return divided_sum


def get_fibonacci_sphere_as_vectors(samples=1):
    points =[]
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
