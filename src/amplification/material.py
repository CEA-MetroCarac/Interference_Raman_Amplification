"""
Material class, has a name and refractive index law.
"""
import os
import sys

import numpy as np

# from common.execution.paths import PATH_DATA_METRO_CARAC
from amplification.aliases import DATAPATH_DAMIEN


class Material:
    """
    Class representing a material. The material name must have a associated csv
    file containing the refractive index information (as an array).
    """

    def __init__(self, name):
        self.index_dir = os.path.join(DATAPATH_DAMIEN,
                                      'data_indices')
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
        # for cx_Freeze
        # see: https://cx-freeze.readthedocs.io/en/stable/faq.html#data-files
        def find_data_file(filename):
            if getattr(sys, "frozen", False):
                # The application is frozen
                datadir = os.path.dirname(sys.executable)
            else:
                # The application is not frozen
                # Change this bit to match where you store your data files:
                datadir = self.index_dir
            return os.path.join(datadir, filename)

        index_file = find_data_file(self.name + '.csv')
        # index_file = os.path.join(self.INDEX_DIR, self.name + '.csv')
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
