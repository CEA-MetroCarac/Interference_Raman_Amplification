"""
Material class, has a name and refractive index law.
"""
import os
import sys
import numpy as np

from amplification import DATA_INDICES


class Material:
    """
    Class representing a material. The material name must have a associated csv
    file containing the refractive index information (as an array).
    """

    def __init__(self, name):
        self.index_dir = DATA_INDICES
        self.name = name
        # self.label = label
        self.refractive_index = self.index_by_name()

    def index_by_name(self):
        """
        Get refractive index via the material name.
        Refractive indices are stored in csv files wavelength // index

        Returns
        -------
        refractive_index: nd.array((3, N))
        Array [[lambda (nm)], [n], [k]]
        """
        index_file = os.path.join(self.index_dir, self.name + '.csv')
        print(index_file)
        try:
            arr = np.loadtxt(fname=index_file,
                             skiprows=1,
                             delimiter=',',
                             unpack=True)
            arr[0] *= 1000
            if arr.shape[0] == 3:
                return arr
            elif arr.shape[0] == 2:
                z = np.zeros((1, arr.shape[1]))
                return np.concatenate((arr, z))
        except Exception as ex:
            print('failed to import material: ' + self.name + ' located at:')
            print(index_file)
            print(ex)

    def index(self, wavelength):
        """
        Returns the material refractive index at a given wavelength (in nm).
        If the wavelength is not part of self.refractive_index, returns an 
        interpolated value.

        Parameters
        ----------
        wavelength: float  
        Wavelength in nm.

        Returns
        -------
        index: complex
        Complex refractive index, using n - jk convention.
        """
        n = np.interp(wavelength,
                      self.refractive_index[0],
                      self.refractive_index[1])
        if self.refractive_index.shape[0] == 3:
            k = np.interp(wavelength,
                          self.refractive_index[0],
                          self.refractive_index[2])
            return n - 1j * k
        elif self.refractive_index.shape[0] == 2:
            return n
        else:
            return False
