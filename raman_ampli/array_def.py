"""
module description
"""
import numpy as np


def array_from_thickness(array, num_integ, step_size):
    """
    Define triangular matrix, according to the thickness of interest and its
    discretization --> reprendre descriptif.
    Parameters
    ----------
    array: 1D numpy array
        blabla
    num_integ: int
        blabla
    step_size: int
        blabla

    Returns
    -------
    Triangular matrix 'matrix'
    """
    len_array = len(array)
    matrix = np.empty((len_array, num_integ))
    matrix[:] = np.nan

    test = 1 + (array[-1] - 0) / step_size
    if test > num_integ:
        print(
            "Change matrix dimension. The discretized layer thickness must "
            "have less elements than num_integ value (axis 0).")
        return
    elif test <= num_integ:
        for i, thick_value in enumerate(array):
            l_partial = np.arange(start=0, stop=thick_value, step=step_size)
            for j, _ in enumerate(l_partial):
                matrix[i, j] = l_partial[j]
        return matrix


def skip_nan(factor_array):
    """
    Formatting of 'factor_array' (containing amplification values). Put '0'
    instead of 'NaN' in the resulting array.
    Parameters
    ----------
    factor_array

    Returns
    -------
    Array 'm', where 'NaN' values have been replaced by '0'.
    """
    matrix = np.where(np.isnan(factor_array), 0, factor_array)
    return matrix
