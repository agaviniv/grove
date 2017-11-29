import numpy as np
import pytest

from grove.alpha.jordan_gradient.gradient_utils import binary_to_real, \
    measurements_to_bf

def test_binary_to_real():
    precision = 9
    decimal_rep = 0.345703125
    binary_rep = 0.010110001

    decimal_convert = binary_to_real(binary_rep)

    assert(np.isclose(decimal_rep, decimal_convert))

def test_measurements_to_bf():
    measurements = [[1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 0, 0]]
    true_bf = 0.01

    bf_from_measurements = measurements_to_bf(measurements)

    assert(np.isclose(true_bf, bf_from_measurements))
