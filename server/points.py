from math import *
import numpy as np
import helper


class Points:

    def get_joint_numerical_range(self, sammples_count=1):
        points = helper.get_fibonacci_sphere_as_vectors(sammples_count)
        jnr_points = []

        for i in range(len(points)):

            point = points[i]
            operators = self.get_prim_operator_and_used_partial_operators(point)

            if len(operators) == 2:

                prim_operator = operators[0]
                partial_operators = operators[1]
                max_eig_vector = self.get_max_eig_vector_of_matrix(prim_operator)

                x = self.get_predicted_value_of_operator(partial_operators[0], max_eig_vector)
                y = self.get_predicted_value_of_operator(partial_operators[1], max_eig_vector)
                z = self.get_predicted_value_of_operator(partial_operators[2], max_eig_vector)

                jnr_points.append((x, y, z))

        return jnr_points


    def get_prim_operator_and_used_partial_operators(self, point):
        #
        # prime_operator - F' form calculation procedure
        # operators - in order F1, F2, F3
        #
        dimension = len(point)
        prime_operator = np.zeros((dimension, dimension))
        operators = []

        for i in range(dimension):

            operator = helper.get_hermitian_operator(dimension)
            operators.append(operator)

            multiplied_operator_by_point = operator * point[i]
            sum_of_multipled_operators = np.add(prime_operator, multiplied_operator_by_point)
            prime_operator = sum_of_multipled_operators

        return prime_operator, operators


    def get_max_eig_vector_of_matrix(self, matrix):

        eigen_values_and_vectors = np.linalg.eigh(matrix)

        if len(eigen_values_and_vectors) == 2:
            last_index_of_eigen_vecctor = len(eigen_values_and_vectors[1]) - 1

            return eigen_values_and_vectors[1][last_index_of_eigen_vecctor]


    def get_predicted_value_of_operator(self, operator, vector):

        sum = 0
        dimension = len(operator)

        if dimension == vector.size:

            for i in range(dimension):
                for j in range(dimension):
                    Xij = operator[i][j]
                    vi_Xij = vector[i] * Xij
                    vi_Xij_vj = vi_Xij * vector[j]
                    sum = np.add(sum, vi_Xij_vj)

            return sum
        return -1
