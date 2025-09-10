"""
Class representing a layer. Ordered layers will form a stack.
"""

import numpy as np

import raman_ampli.material as m


class Layer():
    """
    Class defining a layer, made of an (n,k) database, a material's name and
    a thickness (in nanometers).
    """

    def __init__(self, mat_filename, label=None, thickness=np.inf):
        self.mat = m.Material(mat_filename)
        if label is None:
            self.label = mat_filename
        else:
            self.label = label
        self.thickness = thickness
        self.is_substrate = False

        if isinstance(thickness, float):
            if thickness == np.inf:
                self.is_substrate = True

    def __str__(self):
        return (self.mat.name + ' / ' + str(self.label) + ' / ' + str(
            self.thickness) + ' nm')
